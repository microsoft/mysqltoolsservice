# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from requests import get

IP_GETTER_URI = "https://api.ipify.org"

def get_public_ip() -> str:
    return get(IP_GETTER_URI).content.decode('utf8')