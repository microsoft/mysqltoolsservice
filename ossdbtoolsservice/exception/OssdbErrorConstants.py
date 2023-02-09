# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""This module holds the error resource constants for ossdb tools service errors"""

class OssdbErrorConstants():

    """ ERROR MESSAGES """
    MYSQL_SSL_CA_REQUIRED_FOR_VERIFY_MODES_ERRMSG = "SSL Connection Error: SSL CA certificate is required if ssl-mode is VERIFY_CA or VERIFY_IDENTITY."

    """ INTERNAL ERROR CODES """
    MYSQL_FLEX_SSL_REQUIRED_NOT_PROVIDED_CODE = 50001
    MYSQL_FLEX_IP_NOT_WHITELISTED_CODE = 50002
    MYSQL_FLEX_INCORRECT_CREDENTIALS_CODE = 50003
    MYSQL_SSL_CA_REQUIRED_FOR_VERIFY_MODES_CODE = 50004
    EXECUTE_QUERY_GET_CONNECTION_ERROR = 50005
    EXECUTE_DEPLOY_GET_CONNECTION_ERROR = 50006
    CANCEL_QUERY_ERROR = 50007
    DISPOSE_QUERY_REQUEST_ERROR = 50008
    UNSUPPORTED_REQUEST_METHOD = 50009
    REQUEST_METHOD_PROCESSING_UNHANDLED_EXCEPTION = -32603
    LIST_DATABASE_GET_CONNECTION_VALUE_ERROR = 50010
    LIST_DATABASE_ERROR = 50011
    EDIT_DATA_CUSTOM_QUERY_UNSUPPORTED_ERROR = 50012
    EDIT_DATA_COMMIT_FAILURE = 50013
    EDIT_DATA_SESSION_NOT_FOUND = 50014
    EDIT_DATA_SESSION_OPERATION_FAILURE = 50015
    GET_METADATA_FAILURE = 50016
    OBJECT_EXPLORER_CREATE_SESSION_ERROR = 50017
    OBJECT_EXPLORER_CLOSE_SESSION_ERROR = 50018
    OBJECT_EXPLORER_EXPAND_NODE_ERROR = 50019
    ANOTHER_QUERY_EXECUTING_ERROR = 50020
    DISPOSE_REQUEST_NO_QUERY_ERROR = 50021
    SAVE_QUERY_RESULT_ERROR = 50022
    SCRIPTAS_REQUEST_ERROR = 50023
    UNKNOWN_CONNECTION_ERROR = 50024
    MYSQL_DRIVER_UNKNOWN_ERROR_CODE = 50025
    NEW_DATABASE_GET_CHARSETS_ERROR_CODE = 50026
    NEW_DATABASE_GET_COLLATIONS_ERROR_CODE = 50027
    NEW_DATABASE_CREATE_ERROR_CODE = 50028
    FIREWALL_RULE_SERVER_DETAILS_NOT_FOUND_ERROR_CODE = 50029
    FIREWALL_RULE_ERROR_CODE = 50030
    PUBLIC_IP_FETCH_ERROR_CODE = 500031
    
    """ ERROR CAUSES """
    MYSQL_FLEX_SSL_REQUIRED_NOT_PROVIDED_CAUSES = "SSL encryption is required by server but is not configured by client."
    MYSQL_FLEX_INCORRECT_CREDENTIALS_CAUSES = "The connection details or credentials provided are invalid."

    """ERROR SUGGESTIONS """
    MYSQL_FLEX_SSL_REQUIRED_NOT_PROVIDED_SUGGESTIONS = "Navigate to \'Advanced Properties\' tab and check that the SSL parameters are correctly configured. \nFor more details on connecting to Azure Database for MySQL using SSL encryptions, see https://learn.microsoft.com/azure/mysql/flexible-server/how-to-connect-tls-ssl"
    MYSQL_FLEX_IP_NOT_WHITELISTED_SUGGESTIONS = "Verify the firewall settings on your Azure Database for MySQL flexible server to allow connections from your client address are configured correctly. \n For more details on firewall configuration, see https://learn.microsoft.com/azure/mysql/flexible-server/how-to-manage-firewall-portal"
    MYSQL_FLEX_INCORRECT_CREDENTIALS_SUGGESTIONS = "Check that the provided connection details and credentials (Server name, User name, Password, SSL cert(if provided)) are correct."
    MYSQL_SSL_CA_REQUIRED_FOR_VERIFY_MODES_SUGGESTIONS = "To connect using these SSL modes, navigate to \'Advanced Properties\' tab and configure the SSL CA certificate. \nFor more details on SSL modes, see https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html"


    # ErrorTelemetryViews
    CONNECTION = 'Connection'
    EDIT_DATA = 'Edit Data'
    JSON_RPC = 'Json Rpc'
    METADATA = 'Metadata'
    OBJECT_EXPLORER = 'Object Explorer'
    QUERY_EXECUTION = 'Query Execution'
    SCRIPTING = 'Scripting'
    FIREWALL_RULE = 'Firewall Rule'

    # ErrorTelmetryNames
    LIST_DATABASES_CONNECTION_VALUE_ERROR = 'List Databases Connection Value Error'
    LIST_DATABASES_ERROR = 'List Databases Error'
    BUILD_CONNECTION_ERROR = 'Build Connection Error'
    EDIT_DATA_CUSTOM_QUERY = 'Edit Data Custom Query Unsupported'
    EDIT_DATA_COMMIT = 'Edit Data Commit Failure'
    EDIT_DATA_SESSION_NOT_FOUND = 'Edit Data Session Not Found'
    EDIT_DATA_SESSION_OPERATION = 'Edit Data Session Operation Failure'
    UNSUPPORTED_REQUEST = 'Unsupported Request Method'
    REQUEST_METHOD_PROCESSING = 'Request Method Processing Unhandled Exception'
    GET_METADATA_FAILURE = 'Get Metadata Failure'
    OBJECT_EXPLORER_CREATE_SESSION = 'Object Explorer Create Session Error'
    OBJECT_EXPLORER_CLOSE_SESSION = 'Object Explorer Close Session Error'
    OBJECT_EXPLORER_EXPAND_NODE = 'Object Explorer Expand Node Error'
    EXECUTE_QUERY_GET_CONNECTION = 'Execute Query Get Connection Error'
    EXECUTE_DEPLOY_GET_CONNECTION = 'Execute Deploy Get Connection Error'
    ANOTHER_QUERY_EXECUTING = 'Another Query Executing Error'
    CANCEL_QUERY = 'Cancel Query'
    DISPOSE_QUERY_NO_QUERY = 'Dispose Query No Query Error'
    DISPOSE_QUERY_REQUEST = 'Dispose Query Request Error'
    SAVE_QUERY_RESULT = 'Save Query Result Error'
    SCRIPT_AS_REQUEST = 'Script As Request Error'
    FIREWALL_RULE_SERVER_DETAILS_NOT_FOUND = 'Server Not Found'
    FIREWALL_RULE_ERROR = "Firewall Rule Error"
    PUBLIC_IP_FETCH_ERROR = "Public Ip Fetch Error"