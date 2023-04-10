# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.utils.constants import DEFAULT_PORT

def is_none_or_empty(value_to_check: str):
    if value_to_check is None or len(value_to_check.strip()) == 0:
        return True
    return False

def validate_params(provider, params):
    if not params.options.get('host') or is_none_or_empty(params.options.get('host')):
        params.options['host'] = 'NULL'
    if not params.options.get('dbname') or is_none_or_empty(params.options.get('dbname')):
        params.options['dbname'] = 'NULL'
    if not params.options.get('user') or is_none_or_empty(params.options.get('user')):
        params.options['user'] = 'NULL'
    if not params.options.get('port') or is_none_or_empty(params.options.get('port')):
        params.options['port'] = DEFAULT_PORT[provider]
    if not params.options.get('authenticationType') or is_none_or_empty(params.options.get('authenticationType')):
        params.options['authenticationType'] = 'NULL'
    if not params.options.get('groupId') or is_none_or_empty(params.options.get('groupId')):
        params.options['groupId'] = 'NULL'

def generate_session_uri(provider, params):
    validate_params(provider, params)
    session_uri = "{0}:{1}:{2}:{3}:{4}:{5}".format(
        params.options['host'],
        params.options['dbname'],
        params.options['user'],
        params.options['port'],
        params.options['authenticationType'],
        params.options['groupId']
    )
    return session_uri