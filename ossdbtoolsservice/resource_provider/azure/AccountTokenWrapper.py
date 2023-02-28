# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import Dict
from ossdbtoolsservice.resource_provider.contracts.account import Account, AccountSecurityToken


class AccountTokenWrapper:

    def __init__(self, account: Account, token_mappings: Dict[str, AccountSecurityToken]):
        self.account: Account = account
        self.security_token_mappings: Dict[str, AccountSecurityToken] = token_mappings
    
    
