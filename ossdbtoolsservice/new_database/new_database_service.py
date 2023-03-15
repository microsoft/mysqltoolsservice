# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from ossdbtoolsservice.connection.contracts.common import ConnectionType
from ossdbtoolsservice.driver.types.driver import ServerConnection
from ossdbtoolsservice.exception.OssdbErrorConstants import OssdbErrorConstants
from ossdbtoolsservice.hosting.json_rpc_server import RequestContext
from ossdbtoolsservice.hosting.service_provider import ServiceProvider
from ossdbtoolsservice.new_database.contracts.charset_info import CharsetInfo
from ossdbtoolsservice.new_database.contracts.create_database_request import CREATE_DATABASE_REQUEST, CreateDatabaseRequest
from ossdbtoolsservice.new_database.contracts.get_charsets_request import GET_CHARSETS_REQUEST, GetCharsetsRequest, GetCharsetsResponse
from ossdbtoolsservice.new_database.contracts.get_collations_request import GET_COLLATIONS_REQUEST, GetCollationsRequest, GetCollationsResponse
from ossdbtoolsservice.query.batch import ResultSetStorageType
from ossdbtoolsservice.query.query import Query, QueryEvents, QueryExecutionSettings
import ossdbtoolsservice.utils.constants as constants


GET_CHARSETS_QUERY = "SELECT CHARACTER_SET_NAME, DEFAULT_COLLATE_NAME from INFORMATION_SCHEMA.CHARACTER_SETS ;"
GET_COLLATIONS_QUERY = "SELECT COLLATION_NAME FROM INFORMATION_SCHEMA.COLLATIONS WHERE CHARACTER_SET_NAME = '{}' ;"
CREATE_DATABASE_QUERY = "CREATE DATABASE `{}`"
CHARSET_SUFFIX_DATABASE_QUERY = " CHARACTER SET = '{}'"
COLLATION_SUFFIX_DATABASE_QUERY = " COLLATE = '{}'"

class NewDatabaseService(object):
    """Service for creating new database"""

    def __init__(self):
        self._service_provider: ServiceProvider = None
        self._service_action_mapping: dict = {
            GET_CHARSETS_REQUEST: self._handle_get_charsets_request,
            GET_COLLATIONS_REQUEST: self._handle_get_collations_request,
            CREATE_DATABASE_REQUEST: self._handle_create_database_request
        }

    def register(self, service_provider: ServiceProvider):
        self._service_provider = service_provider
        # Register the request handlers with the server

        for action in self._service_action_mapping:
            self._service_provider.server.set_request_handler(action, self._service_action_mapping[action])

        if self._service_provider.logger is not None:
            self._service_provider.logger.info('New database service successfully initialized')

    def _handle_get_charsets_request(self, request_context: RequestContext, params: GetCharsetsRequest):
        query_str = GET_CHARSETS_QUERY
        connection = self._get_connection_for_query(params.owner_uri)
        try:
            columns, rows = connection.execute_dict(query=query_str, throw_exception=True)
            request_context.send_response(self._build_get_charsets_response(columns, rows))
        except Exception as e:
            request_context.send_unhandled_error_response(e, OssdbErrorConstants.NEW_DATABASE_GET_CHARSETS_ERROR_CODE)
    
    def _handle_get_collations_request(self, request_context: RequestContext, params: GetCollationsRequest):
        query_str = GET_COLLATIONS_QUERY.format(params.charset)
        connection = self._get_connection_for_query(params.owner_uri)
        try:
            columns, rows = connection.execute_dict(query=query_str, throw_exception=True)
            request_context.send_response(self._build_get_collations_response(columns, rows))
        except Exception as e:
            request_context.send_unhandled_error_response(e, OssdbErrorConstants.NEW_DATABASE_GET_COLLATIONS_ERROR_CODE)
    
    def _handle_create_database_request(self, request_context: RequestContext, params: CreateDatabaseRequest):
        query_str = self._build_create_database_query(params)
        connection = self._get_connection_for_query(params.owner_uri)
        try:
            connection.execute_dict(query=query_str, throw_exception=True)
            request_context.send_response(None)
        except Exception as e:
            request_context.send_unhandled_error_response(e, OssdbErrorConstants.NEW_DATABASE_CREATE_ERROR_CODE)
    
    def _create_query(self, owner_uri: str, query_str: str) -> Query :
        return Query(
            owner_uri,
            query_str,
            QueryExecutionSettings(None, ResultSetStorageType.FILE_STORAGE),
            QueryEvents()
        )

    def _get_connection_for_query(self, owner_uri: str) -> ServerConnection :
        connection_service = self._service_provider[constants.CONNECTION_SERVICE_NAME]
        return connection_service.get_connection(owner_uri, ConnectionType.QUERY)

    def _build_get_charsets_response(self, columns: list[str], rows: list[dict]) -> GetCharsetsResponse :
        charsets = []
        for row in rows :
            charsets.append(CharsetInfo(row[columns[0]], row[columns[1]]))
        return GetCharsetsResponse(charsets)
    
    def _build_get_collations_response(self, columns: list[str], rows: list[dict]) -> GetCollationsResponse :
        collations = []
        for row in rows :
            collations.append(row[columns[0]])
        return GetCollationsResponse(collations)
    
    def _build_create_database_query(self, params: CreateDatabaseRequest) -> str :
        query_text = CREATE_DATABASE_QUERY.format(params.db_name)
        if params.charset :
            query_text += CHARSET_SUFFIX_DATABASE_QUERY.format(params.charset)
            if params.collation :
                query_text += COLLATION_SUFFIX_DATABASE_QUERY.format(params.collation)
        return query_text
