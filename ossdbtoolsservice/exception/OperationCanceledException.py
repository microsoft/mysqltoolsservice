# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .OssdbErrorConstants import OssdbErrorConstants

class OperationCanceledException(Exception):

    def __init__(self):
        super().__init__(OssdbErrorConstants.OPERATION_CANCELED_EXCEPTION)
