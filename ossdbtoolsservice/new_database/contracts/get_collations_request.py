# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import List

from ossdbtoolsservice.hosting import IncomingMessageConfiguration
from ossdbtoolsservice.serialization import Serializable


class GetCollationsRequest(Serializable):

    def __init__(self):
        self.owner_uri: str = None
        self.charset: str = None


class GetCollationsResponse:

    def __init__(self, collations: List[str]):
        self.collations = collations


GET_COLLATIONS_REQUEST = IncomingMessageConfiguration('mysqlnewdatabase/collations', GetCollationsRequest)