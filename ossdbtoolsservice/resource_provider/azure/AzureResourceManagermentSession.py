# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from ossdbtoolsservice.resource_provider.azure.credentials.BearerTokenCredential import BearerTokenCredential
from ossdbtoolsservice.resource_provider.contracts.account import AccountSecurityToken
from azure.mgmt.rdbms.mysql_flexibleservers import MySQLManagementClient
from azure.mgmt.resourcegraph import ResourceGraphClient

class AzureResourceManagementSession:

    def __init__(self, token: AccountSecurityToken, base_url: str):
        self._credentials = BearerTokenCredential(token.token, token.expires_on)
        self._base_url = base_url

    def get_mysql_management_client(self, subscription_id: str) -> MySQLManagementClient:
        return MySQLManagementClient(self._credentials, subscription_id, self._base_url)
    
    def get_resource_graph_client(self) -> ResourceGraphClient:
        return ResourceGraphClient(self._credentials, self._base_url)
