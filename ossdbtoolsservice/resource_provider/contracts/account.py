# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import List
from ossdbtoolsservice.serialization import Serializable

class Account(Serializable):

    @classmethod
    def get_child_serializable_types(cls):
        return {'key': AccountKey, 'display_info': AccountDisplayInfo, 'properties': AccountProperties}

    def __init__(self):
        self.key: AccountKey = None
        self.display_info: AccountDisplayInfo = None
        self.properties: AccountProperties = None
        self.is_stale: bool = None
    
    @classmethod
    def ignore_extra_attributes(cls):
        return True

class AccountSecurityToken(Serializable):

    def __init__(self):
        self.expires_on: str = None
        self.token: str = None
        self.token_type: str = None
        self.resource: str = None
    
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

class AccountProperties(Serializable):

    @classmethod
    def get_child_serializable_types(cls):
        return {'tenants': Tenant, 'owning_tenant': Tenant, 'provider_settings': ProviderSettings}

    def __init__(self):
        self.is_ms_account: bool = None
        self.owning_tenant: Tenant = None
        self.tenants: List[Tenant] = []
        self.provider_settings: ProviderSettings = None

    @classmethod
    def ignore_extra_attributes(cls):
        return True

class Tenant(Serializable):

    def __init__(self):
        self.id: str = None
        self.display_name: str = None
        self.user_id: str = None

    @classmethod
    def ignore_extra_attributes(cls):
        return True

class ProviderSettings(Serializable):

    @classmethod
    def get_child_serializable_types(cls):
        return {'settings': ProviderSettingsObject}

    def __init__(self):
        self.id: str = None
        self.display_name: str = None
        self.settings: ProviderSettingsObject = None

    @classmethod
    def ignore_extra_attributes(cls):
        return True

class ProviderSettingsObject(Serializable):

    @classmethod
    def get_child_serializable_types(cls):
        return {'arm_resource': ResourceSettings, 'graph_resource': ResourceSettings, 'oss_rdbms_resource': ResourceSettings}

    def __init__(self):
        self.arm_resource: ResourceSettings = None
        self.graph_resource: ResourceSettings = None
        self.oss_rdbms_resource: ResourceSettings = None
        self.host: str = None
        self.client_id: str = None

    @classmethod
    def ignore_extra_attributes(cls):
        return True

class ResourceSettings(Serializable):

    def __init__(self):
        self.id: str = None
        self.endpoint: str = None

    @classmethod
    def ignore_extra_attributes(cls):
        return True