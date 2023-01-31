# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.serialization import Serializable

class Account(Serializable):

    @classmethod
    def get_child_serializable_types(cls):
        return {'key': AccountKey, 'display_info': AccountDisplayInfo}

    def __init__(self):
        self.key: AccountKey = None
        self.display_info: AccountDisplayInfo = None
        self.properties = None
        self.is_stale: bool = None
        self.delete: bool = None
    
    @classmethod
    def ignore_extra_attributes(cls):
        return True
        
class AccountKey(Serializable):
    
    def __init__(self):
        self.provider_id: str = None
        self.provider_args = None
        self.account_id: str = None
        self.account_version: str = None
    
    @classmethod
    def ignore_extra_attributes(cls):
        return True
        
class AccountDisplayInfo(Serializable):
    
    def __init__(self):
        self.contextual_display_name: str = None
        self.account_type: str = None
        self.display_name: str = None
        self.user_id: str = None
        self.email: str = None
        self.name: str = None
    
    @classmethod
    def ignore_extra_attributes(cls):
        return True