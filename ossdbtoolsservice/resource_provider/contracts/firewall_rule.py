# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import Dict
from ossdbtoolsservice.hosting import IncomingMessageConfiguration
from ossdbtoolsservice.resource_provider.contracts.account import Account, AccountSecurityToken
from ossdbtoolsservice.serialization import Serializable

class HandleFirewallRuleRequest(Serializable):

    def __init__(self):
        self.error_code: int = None
        self.error_message: str = None
        self.connection_type_id: str = None

class HandleFirewallRuleResponse:
    
    def __init__(self, handle, error_message=None, ip_address=None):
        self.result: bool = handle
        self.error_message: str = error_message
        self.ip_address: str = ip_address

class CreateFirewallRuleRequest(Serializable):
    
    @classmethod
    def get_child_serializable_types(cls):
        return {'account': Account}

    def __init__(self):
        self.account: Account = None
        self.server_name: str = None
        self.start_ip_address: str = None
        self.end_ip_address: str = None
        self.firewall_rule_name: str = None
        self.security_token_mappings = None

class CreateFirewallRuleResponse:
    
    def __init__(self, success, error_message=None):
        self.result: bool = success
        self.error_message: str = error_message

HANDLE_FIREWALL_RULE_REQUEST = IncomingMessageConfiguration('resource/handleFirewallRule', HandleFirewallRuleRequest)

CREATE_FIREWALL_RULE_REQUEST = IncomingMessageConfiguration('resource/createFirewallRule', CreateFirewallRuleRequest)