# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import List

from ossdbtoolsservice.hosting import IncomingMessageConfiguration
from ossdbtoolsservice.serialization import Serializable


class GetCharsetsRequest(Serializable):

    def __init__(self):
        self.owner_uri: str = None


class GetCharsetsResponse:

    def __init__(self, charsets: List[str]):
        self.charsets = charsets


GET_CHARSETS_REQUEST = IncomingMessageConfiguration('mysqlnewdatabase/charsets', GetCharsetsRequest)