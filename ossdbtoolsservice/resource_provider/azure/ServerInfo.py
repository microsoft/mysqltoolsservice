# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from ossdbtoolsservice.serialization.serializable import Serializable


class ServerInfo(Serializable):

    def __init__(self):
        self.id = None
        self.name = None
        self.tenant_id = None
        self.location = None
        self.resource_group = None
        self.subscription_id = None

    @classmethod
    def ignore_extra_attributes(cls):
        return True
