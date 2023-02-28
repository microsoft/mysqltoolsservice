# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from ossdbtoolsservice.resource_provider.azure.AccountTokenWrapper import AccountTokenWrapper
from ossdbtoolsservice.resource_provider.azure.AzureResourceManagermentSession import AzureResourceManagementSession
from ossdbtoolsservice.resource_provider.azure.ServerInfo import ServerInfo
from azure.mgmt.resourcegraph.models import QueryRequest, QueryResponse
from azure.mgmt.rdbms.mysql_flexibleservers.models import FirewallRule

from ossdbtoolsservice.resource_provider.azure.poller.arm_pollers import ARMPollingOverrideRetryAfter

GET_SERVERS_RESOURCE_GRAPH_QUERY = "Resources | where type =~ 'Microsoft.DBforMySQL/flexibleServers'| where name == '{}'"
FIREWALL_POLLER_TIMEOUT = 15

class AzureResourceManager:
    
    def __init__(self) -> None:
        pass

    def create_session(self, account_token_wrapper: AccountTokenWrapper) -> AzureResourceManagementSession:
        tenant_id = account_token_wrapper.account.properties.owning_tenant.id
        token = account_token_wrapper.security_token_mappings[tenant_id]
        base_url = account_token_wrapper.account.properties.provider_settings.settings.arm_resource.endpoint
        return AzureResourceManagementSession(token, base_url)

    def fetch_server_details(self, session: AzureResourceManagementSession, server_name: str) -> ServerInfo:
        client = session.get_resource_graph_client()
        query = QueryRequest(query=GET_SERVERS_RESOURCE_GRAPH_QUERY.format(server_name))
        response: QueryResponse = client.resources(query)
        if response.total_records == 0:
            return None
        else:
            return self._build_server_info(response.data[0])
    
    def create_firewall_rule(self, session: AzureResourceManagementSession, server: ServerInfo, start_ip: str, end_ip: str, rule_name: str) -> None:
        client = session.get_mysql_management_client(server.subscription_id)
        client.firewall_rules.begin_create_or_update(
            server.resource_group, 
            server.name, rule_name, 
            FirewallRule(start_ip_address=start_ip, end_ip_address=end_ip),
            polling=ARMPollingOverrideRetryAfter(FIREWALL_POLLER_TIMEOUT)).result()
        
    def _build_server_info(self, server_details_dict: dict) -> ServerInfo:
        return ServerInfo.from_dict(server_details_dict)