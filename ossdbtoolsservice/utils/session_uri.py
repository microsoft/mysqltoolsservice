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
        params.options['host'] if not params.options.get('host') or is_none_or_empty(params.options.get('host')) else 'NULL',
        params.options['dbname'] if not params.options.get('dbname') or is_none_or_empty(params.options.get('dbname')) else 'NULL',
        params.options['user'] if not params.options.get('user') or is_none_or_empty(params.options.get('user')) else 'NULL',
        params.options['port'] if not params.options.get('port') or is_none_or_empty(params.options.get('port')) else 'NULL',
        params.options['authenticationType'] if not params.options.get('authenticationType') or is_none_or_empty(params.options.get('authenticationType')) else 'NULL',
        params.options['groupId'] if not params.options.get('groupId') or is_none_or_empty(params.options.get('groupId')) else 'NULL'
    )
    return session_uri