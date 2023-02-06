# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from typing import Dict
from ossdbtoolsservice.resource_provider.azure.credentials.BearerTokenCredential import BearerTokenCredential
from ossdbtoolsservice.resource_provider.contracts.account import AccountSecurityToken
from azure.mgmt.rdbms.mysql_flexibleservers import MySQLManagementClient
from azure.mgmt.resourcegraph import ResourceGraphClient

class AzureResourceManagementSession:

    def __init__(self, token: AccountSecurityToken, base_url: str):
        self._credentials = BearerTokenCredential(token.token, token.expires_on)
        self._base_url = base_url
        self._mysql_management_clients: Dict[str, MySQLManagementClient] = dict()
        self._resource_graph_client: ResourceGraphClient = None

    def get_mysql_management_client(self, subscription_id: str) -> MySQLManagementClient:
        if not subscription_id in self._mysql_management_clients:
            self._mysql_management_clients[subscription_id] = MySQLManagementClient(self._credentials, subscription_id, self._base_url)
        return self._mysql_management_clients[subscription_id]
    
    def get_resource_graph_client(self) -> ResourceGraphClient:
        if self._resource_graph_client == None:
            self._resource_graph_client = ResourceGraphClient(self._credentials, self._base_url)
        return self._resource_graph_client
    
    def close(self):
        # Close mysql management clients
        for sub_id in self._mysql_management_clients:
            self._close_client(self._mysql_management_clients[sub_id]) 
        
        # Close resource graph client
        self._close_client(self._resource_graph_client)
            
                    
    def _close_client(self, client):
        try:
            client.close()
        except:
            # do nothing on exception
            return
            
