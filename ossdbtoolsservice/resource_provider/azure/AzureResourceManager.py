# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from ossdbtoolsservice.resource_provider.azure.AzureResourceManagermentSession import AzureResourceManagementSession
from ossdbtoolsservice.resource_provider.azure.ServerInfo import ServerInfo

GET_SERVERS_RESOURCE_GRAPH_QUERY = "Resources | where type =~ 'Microsoft.DBforMySQL/flexibleServers'| where name == '{}'"

class AzureResourceManager:
    
    def create_session(self, token: str, expires_on: str, base_url: str) -> AzureResourceManagementSession:
        return AzureResourceManagementSession(token, expires_on, base_url)

    def fetch_server_details(self, session: AzureResourceManagementSession, server_name: str) -> ServerInfo:
        client = session.get_resource_graph_client()
        query = client.operations.models.QueryRequest(GET_SERVERS_RESOURCE_GRAPH_QUERY.format(server_name))
        response = client.resources(query)
        return self._build_server_info(response)
    
    def create_firewall_rule(self, session: AzureResourceManagementSession, server: ServerInfo, start_ip: str, end_ip: str) -> None:
        return None
        
    def _build_server_info(self, response) -> ServerInfo:
        return ServerInfo()