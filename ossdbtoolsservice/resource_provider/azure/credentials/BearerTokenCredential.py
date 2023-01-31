# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from typing import Any, Optional
from azure.core.credentials import TokenCredential, AccessToken

class BearerTokenCredential(TokenCredential):

    def __init__(self, token: str, expiresOn: int) -> None:
        self.accessToken = AccessToken(token, expiresOn)
    
    def get_token(
        self,
        *scopes: str,
        claims: Optional[str] = None,
        tenant_id: Optional[str] = None,
        **kwargs: Any
    ) -> AccessToken:
        return self.accessToken