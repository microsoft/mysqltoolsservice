# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def is_not_none_or_empty(value_to_check: str):
    if value_to_check is None or len(value_to_check.strip()) == 0:
        return False
    return True

def generate_session_uri(params):
    session_uri = "{0}:{1}:{2}:{3}:{4}:{5}".format(
        params.options['host'] if is_not_none_or_empty(params.options['host']) else "NULL",
        params.options['dbname'] if is_not_none_or_empty(params.options['dbname']) else "NULL",
        params.options['user'] if is_not_none_or_empty(params.options['user']) else "NULL",
        params.options['port'] if is_not_none_or_empty(str(params.options['port'])) else "NULL",
        params.options['authenticationType'] if is_not_none_or_empty(params.options['authenticationType']) else "NULL",
        params.options['groupId'] if is_not_none_or_empty(params.options['groupId']) else "NULL"
    )
    return session_uri