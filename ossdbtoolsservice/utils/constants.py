# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""Module containing constants used throughout the service"""

MYSQL_PROVIDER_NAME = 'MySQL'
MARIADB_PROVIDER_NAME = 'MariaDB'
MSSQL_PROVIDER_NAME = 'MSSQL'

SUPPORTED_PROVIDERS = [MYSQL_PROVIDER_NAME, MARIADB_PROVIDER_NAME]

DEFAULT_DB = {
    MYSQL_PROVIDER_NAME: "",
    MARIADB_PROVIDER_NAME: ""
}

DEFAULT_PORT = {
    MYSQL_PROVIDER_NAME: 3306,
    MARIADB_PROVIDER_NAME: 3306
}

# Service names
ADMIN_SERVICE_NAME = 'admin'
CAPABILITIES_SERVICE_NAME = 'capabilities'
CONNECTION_SERVICE_NAME = 'connection'
LANGUAGE_SERVICE_NAME = 'language_service'
METADATA_SERVICE_NAME = 'metadata'
OBJECT_EXPLORER_NAME = 'object_explorer'
QUERY_EXECUTION_SERVICE_NAME = 'query_execution'
SCRIPTING_SERVICE_NAME = 'scripting'
WORKSPACE_SERVICE_NAME = 'workspace'
EDIT_DATA_SERVICE_NAME = 'edit_data'
TASK_SERVICE_NAME = 'tasks'

NEW_DATABASE_SERVICE_NAME = 'new_database'

# ErrorTelemetryViews
CONNECTION = 'Connection'
EDIT_DATA = 'Edit Data'
JSON_RPC = 'Json Rpc'
METADATA = 'Metadata'
OBJECT_EXPLORER = 'Object Explorer'
QUERY_EXECUTION = 'Query Execution'
SCRIPTING = 'Scripting'

# ErrorTelmetryNames
LIST_DATABASES_CONNECTION_VALUE_ERROR = 'List Databases Connection Value Error'
LIST_DATABASES_ERROR = 'List Databases Error'
BUILD_CONNECTION_ERROR = 'Build Connection Error'
EDIT_DATA_CUSTOM_QUERY = 'Edit Data Custom Query'
EDIT_DATA_COMMIT = 'Edit Data Commit'
EDIT_DATA_SESSION_NOT_FOUND = 'Edit Data Session Not Found'
EDIT_DATA_SESSION_OPERATION = 'Edit Data Session Operation'
UNSUPPORTED_REQUEST = 'Unsupported Request'
REQUEST_METHOD_PROCESSING = 'Request Method Processing'
GET_METADATA_FAILURE = 'Get Metadata Failure'
OBJECT_EXPLORER_CREATE_SESSION = 'Object Explorer Create Session'
OBJECT_EXPLORER_CLOSE_SESSION = 'Object Explorer Close Session'
OBJECT_EXPLORER_EXPAND_NODE = 'Object Explorer Expand Node'
EXECUTE_QUERY_GET_CONNECTION = 'Execute Query Get Connection'
EXECUTE_DEPLOY_GET_CONNECTION = 'Execute Deploy Get Connection'
ANOTHER_QUERY_EXECUTING = 'Another Query Executing'
CANCEL_QUERY = 'Cancel Query'
DISPOSE_QUERY_NO_QUERY = 'Dispose Query No Query'
DISPOSE_QUERY_REQUEST = 'Dispose Query Request'
SAVE_QUERY_RESULT = 'Save Query Result'
SCRIPT_AS_REQUEST = 'Script As Request'
