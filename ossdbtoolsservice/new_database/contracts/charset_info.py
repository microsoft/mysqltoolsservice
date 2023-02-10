# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.serialization import Serializable


class CharsetInfo(Serializable):

    def __init__(self, name: str = None, default_collation: str = None):
        self.name: str = name
        self.default_collation: str = default_collation