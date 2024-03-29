# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from enum import Enum
from typing import List  # noqa
from datetime import datetime

import uuid
import sqlparse

from ossdbtoolsservice.driver import ServerConnection
from ossdbtoolsservice.utils.time import get_time_str, get_elapsed_time_str
from ossdbtoolsservice.query.contracts import BatchSummary, SaveResultsRequestParams, SelectionData
from ossdbtoolsservice.query.result_set import ResultSet  # noqa
from ossdbtoolsservice.query.file_storage_result_set import FileStorageResultSet
from ossdbtoolsservice.query.in_memory_result_set import InMemoryResultSet
from ossdbtoolsservice.query.data_storage import FileStreamFactory
from ossdbtoolsservice.utils.cancellation import CancellationToken
from ossdbtoolsservice.exception.OperationCanceledException import OperationCanceledException
from ossdbtoolsservice.query.result_set import ResultSetEvents

class ResultSetStorageType(Enum):
    IN_MEMORY = 1,
    FILE_STORAGE = 2


class BatchEvents:

    def __init__(self, on_execution_started=None, on_execution_completed=None, on_batch_message_sent=None, on_result_set_available=None, on_result_set_updated=None, on_result_set_completed=None):
        self._on_execution_started = on_execution_started
        self._on_execution_completed = on_execution_completed
        self._on_batch_message_sent = on_batch_message_sent
        self._on_result_set_available = on_result_set_available
        self._on_result_set_updated = on_result_set_updated
        self._on_result_set_completed = on_result_set_completed


class SelectBatchEvents(BatchEvents):

    def __init__(self, on_execution_started, on_execution_completed, on_result_set_completed, on_after_first_fetch):
        BatchEvents.__init__(self, on_execution_started, on_execution_completed, on_result_set_completed)
        self._on_after_first_fetch = on_after_first_fetch


class Batch:

    def __init__(
            self,
            batch_text: str,
            ordinal: int,
            selection: SelectionData,
            batch_events: BatchEvents = None,
            storage_type: ResultSetStorageType = ResultSetStorageType.FILE_STORAGE
    ) -> None:
        self.id = ordinal
        self.selection = selection
        self.batch_text = batch_text

        self._execution_start_time: datetime = None
        self._has_error = False
        self._has_executed = False
        self._execution_end_time: datetime = None
        self._result_set: ResultSet = None
        self._notices: List[str] = []
        self._batch_events = batch_events
        self._storage_type = storage_type

    @property
    def batch_summary(self) -> BatchSummary:
        return BatchSummary.from_batch(self)

    @property
    def has_error(self) -> bool:
        return self._has_error

    @property
    def has_executed(self) -> bool:
        return self._has_executed

    @property
    def start_date_str(self) -> str:
        if self._execution_start_time is None:
            return None
        return self._execution_start_time.isoformat()

    @property
    def start_time(self) -> str:
        return get_time_str(self._execution_start_time)

    @property
    def end_time(self) -> str:
        return get_time_str(self._execution_end_time)

    @property
    def elapsed_time(self) -> str:
        return get_elapsed_time_str(self._execution_start_time, self._execution_end_time)

    @property
    def result_set(self) -> ResultSet:
        return self._result_set

    @property
    def row_count(self) -> int:
        return self.result_set.row_count if self.result_set is not None else -1

    @property
    def notices(self) -> List[str]:
        return self._notices

    def get_cursor(self, connection: ServerConnection):
        return connection.cursor(buffered=False)

    def execute(self, conn: ServerConnection, cancellation_token: CancellationToken) -> None:
        """
        Execute the batch using a cursor retrieved from the given connection

        :raises DatabaseError: if an error is encountered while running the batch's query
        """

        if self.has_executed:
            raise Exception("Batch has already executed!")
        
        self._execution_start_time = datetime.now()

        # Call the Batch Execution started callback
        if self._batch_events and self._batch_events._on_execution_started:
            self._batch_events._on_execution_started(self)
        
        try:
            self.doExecute(conn, cancellation_token)
        except Exception as e:
            self._has_error = True
            raise e
        finally:
            self._has_executed = True
            self._execution_end_time = datetime.now()

            # Call the Batch execution completed callback
            if self._batch_events and self._batch_events._on_execution_completed:
                self._batch_events._on_execution_completed(self)

    def doExecute(self, conn: ServerConnection, cancellation_token: CancellationToken):
        try:
            if cancellation_token.canceled:
                raise OperationCanceledException()
            
            cursor = self.get_cursor(conn)
            cursor.execute(self.batch_text)
            self.after_execute(cursor, cancellation_token)
        finally:
            # We are doing this because when the execute fails for named cursors
            # cursor is not activated on the server which results in failure on close
            # Hence we are checking if the cursor was really executed for us to close it
            if cursor and cursor.rowcount != -1 and cursor.rowcount is not None:
                cursor.close()

    def after_execute(self, cursor, cancellation_token: CancellationToken) -> None:
        if cursor.description is not None:
            self.create_result_set(cursor, cancellation_token)

    def create_result_set(self, cursor, cancellation_token: CancellationToken):
        resultset_events = ResultSetEvents(self._batch_events._on_result_set_available, self._batch_events._on_result_set_updated, self._batch_events._on_result_set_completed)
        self._result_set = create_result_set(self._storage_type, 0, self.id, resultset_events)
        self._result_set.read_result_to_end(cursor, cancellation_token)

    def get_subset(self, start_index: int, end_index: int):
        return self._result_set.get_subset(start_index, end_index)

    def save_as(self, params: SaveResultsRequestParams, file_factory: FileStreamFactory, on_success, on_failure) -> None:

        if params.result_set_index != 0:
            raise IndexError('Result set index should be always 0')

        self._result_set.save_as(params, file_factory, on_success, on_failure)


class SelectBatch(Batch):

    def __init__(self, batch_text: str, ordinal: int, selection: SelectionData, batch_events: SelectBatchEvents, storage_type: ResultSetStorageType) -> None:
        Batch.__init__(self, batch_text, ordinal, selection, batch_events, storage_type)

    def get_cursor(self, connection: ServerConnection):
        return connection.cursor(buffered=False)

    def after_execute(self, cursor, cancellation_token: CancellationToken) -> None:
        super().create_result_set(cursor, cancellation_token)


def create_result_set(storage_type: ResultSetStorageType, result_set_id: int, batch_id: int, resultset_events: ResultSetEvents) -> ResultSet:

    if storage_type is ResultSetStorageType.FILE_STORAGE:
        return FileStorageResultSet(result_set_id, batch_id, resultset_events)

    return InMemoryResultSet(result_set_id, batch_id, resultset_events)


def create_batch(batch_text: str, ordinal: int, selection: SelectionData, batch_events: BatchEvents, storage_type: ResultSetStorageType) -> Batch:
    sql = sqlparse.parse(batch_text)
    statement = sql[0]

    if statement.get_type().lower() == 'select':
        into_checker = [True for token in statement.tokens if token.normalized == 'INTO']
        cte_checker = [True for token in statement.tokens if token.ttype == sqlparse.tokens.Keyword.CTE]
        if len(into_checker) == 0 and len(cte_checker) == 0:  # SELECT INTO and CTE keywords can't be used in named cursor
            return SelectBatch(batch_text, ordinal, selection, batch_events, storage_type)

    return Batch(batch_text, ordinal, selection, batch_events, storage_type)
