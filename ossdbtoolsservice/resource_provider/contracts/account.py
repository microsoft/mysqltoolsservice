# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.serialization import Serializable

class Account(Serializable):

    def __init__(self):
        self.key: AccountKey = None
        self.display_info: AccountDisplayInfo = None
        self.properties = None
        self.is_stale: bool = None
        self.delete: bool = None
        
class AccountKey(Serializable):
    
    def __init__(self):
        self.provider_id: str = None
        self.provider_args = None
        self.account_id: str = None
        self.account_version: str = None
        
class AccountDisplayInfo(Serializable):
    
    def __init__(self):
        self.contextual_display_name: str = None
        self.account_type: str = None
        self.display_name: str = None
        self.user_id: str = None
        self.email: str = None
        self.name: str = None