# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .OssdbErrorResource import OssdbErrorResource


class OssdbToolsServiceException(Exception):

    def __init__(self, errorResource: OssdbErrorResource):
        self._errorResource = errorResource
        self._errorCode = self._errorResource.internalErrorCode
        self._errMsg = self._errorResource.errmsg
        super().__init__(self._errorResource.userErrMsg)

    def __str__(self) -> str:
        return super().__str__()

    @property
    def errorCode(self) -> int:
        return self._errorCode

    @property
    def errorMsg(self) -> str:
        return self._errMsg