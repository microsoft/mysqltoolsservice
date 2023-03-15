# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.hosting import IncomingMessageConfiguration
from ossdbtoolsservice.serialization import Serializable

class ColumnInfo():
    def __init__(self, name: str, data_type_name: str) -> None:
        self.name = name
        self.data_type_name = data_type_name

class SerializeDataStartRequestParams(Serializable):
    def __init__(self, save_format: str, file_path: str, rows, is_last: bool):
        self.sava_format = save_format
        self.file_path = file_path
        self.rows = rows
        self.is_last_batch = is_last
        self.columns = None

class SerializeDataContinueRequestParams(Serializable):
    def __init__(self, file_path: str, rows, is_last_batch: bool) -> None:
        self.file_path = file_path
        self.rows = rows
        self.is_last_batch = is_last_batch

class SerializeDataResult():
    def __init__(self, messages: str, succeeded: bool):
        self.messages = messages
        self.succeeded = succeeded

class SerializationOptionsHelper():
    IncludeHeaders = "includeHeaders";
    Delimiter = "delimiter";
    LineSeparator = "lineSeparator";
    TextIdentifier = "textIdentifier";
    Encoding = "encoding";
    Formatted = "formatted";
    MaxCharsToStore = "maxchars";


SERIALIZE_START_REQUEST = IncomingMessageConfiguration('serialize/start', SerializeDataStartRequestParams)
SERIALIZE_CONTINUE_REQUEST = IncomingMessageConfiguration('serialize/continue', SerializeDataContinueRequestParams)
