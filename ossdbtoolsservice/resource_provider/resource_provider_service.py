# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.exception.OssdbErrorConstants import OssdbErrorConstants
from ossdbtoolsservice.hosting.json_rpc_server import RequestContext
from ossdbtoolsservice.hosting.service_provider import ServiceProvider
from ossdbtoolsservice.resource_provider.azure.AccountTokenWrapper import AccountTokenWrapper
from ossdbtoolsservice.resource_provider.azure.AzureResourceManager import AzureResourceManager
from ossdbtoolsservice.resource_provider.contracts.account import AccountSecurityToken
from ossdbtoolsservice.resource_provider.contracts.firewall_rule  import HANDLE_FIREWALL_RULE_REQUEST, CREATE_FIREWALL_RULE_REQUEST, HandleFirewallRuleRequest, HandleFirewallRuleResponse, CreateFirewallRuleRequest, CreateFirewallRuleResponse
from ossdbtoolsservice.utils.ip import get_public_ip
from ossdbtoolsservice.utils.constants import MYSQL_PROVIDER_NAME

class ResourceProviderService(object):
    """Service for resource provider"""

    def __init__(self):
        self._service_provider: ServiceProvider = None
        self._service_action_mapping: dict = {
            HANDLE_FIREWALL_RULE_REQUEST: self._handle_handle_firewall_rule_request,
            CREATE_FIREWALL_RULE_REQUEST: self._handle_create_firewall_rule_request
        }
        self._resource_manager: AzureResourceManager = AzureResourceManager()

    def register(self, service_provider: ServiceProvider):
        self._service_provider = service_provider
        # Register the request handlers with the server

        for action in self._service_action_mapping:
            self._service_provider.server.set_request_handler(action, self._service_action_mapping[action])

        if self._service_provider.logger is not None:
            self._service_provider.logger.info('Resource provider service successfully initialized')
    
    def _handle_handle_firewall_rule_request(self, request_context: RequestContext, params: HandleFirewallRuleRequest):
        try:
            if params.connection_type_id and params.connection_type_id == MYSQL_PROVIDER_NAME and params.error_code and params.error_code == OssdbErrorConstants.MYSQL_FLEX_IP_NOT_WHITELISTED_CODE:
                ipaddr = get_public_ip()
                response = HandleFirewallRuleResponse(handle=True, ip_address=ipaddr)
            else:
                response = HandleFirewallRuleResponse(handle=False)
        except Exception as e:
            response = HandleFirewallRuleResponse(handle=False, error_message=str(e))
                
        request_context.send_response(response)
        
    def _handle_create_firewall_rule_request(self, request_context: RequestContext, params: CreateFirewallRuleRequest):
        try:
            server_name = params.server_name.split(".mysql.database.azure.com")[0]
            account_token_wrapper = self._build_account_token_wrapper(params)
            session = self._resource_manager.create_session(account_token_wrapper)
            server_info = self._resource_manager.fetch_server_details(session, server_name)
            if server_info:
                self._resource_manager.create_firewall_rule(session, server_info, params.start_ip_address, params.end_ip_address, params.firewall_rule_name)
                response = CreateFirewallRuleResponse(success=True)
            else :
                response = CreateFirewallRuleResponse(success=False, error_message="Server details not found")
        except Exception as e:
            response = CreateFirewallRuleResponse(success=False, error_message=str(e))
        
        request_context.send_response(response)
    
    def _build_account_token_wrapper(self, params: CreateFirewallRuleRequest) -> AccountTokenWrapper:
        return AccountTokenWrapper(
            params.account,
            {tenant_id:AccountSecurityToken.from_dict(params.security_token_mappings[tenant_id]) for tenant_id in params.security_token_mappings}
        )