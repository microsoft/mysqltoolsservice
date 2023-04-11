# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def is_none_or_empty(value_to_check: str):
    if value_to_check is None or len(value_to_check.strip()) == 0:
        return True
    return False

def generate_session_uri(params):
    session_uri = "{0}:{1}:{2}:{3}:{4}:{5}".format(
        params.options['host'] if params.options.get('host') and not is_none_or_empty(params.options.get('host')) else 'NULL',
        params.options['dbname'] if params.options.get('dbname') and not is_none_or_empty(params.options.get('dbname')) else 'NULL',
        params.options['user'] if params.options.get('user') and not is_none_or_empty(params.options.get('user')) else 'NULL',
        params.options['port'] if params.options.get('port') and not is_none_or_empty(str(params.options.get('port'))) else 'NULL',
        params.options['authenticationType'] if params.options.get('authenticationType') and not is_none_or_empty(params.options.get('authenticationType')) else 'NULL',
        params.options['groupId'] if params.options.get('groupId') and not is_none_or_empty(params.options.get('groupId')) else 'NULL'
    )
    return session_uri