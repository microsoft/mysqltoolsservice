# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""Module containing utilities for cancelling requests"""


class CancellationToken:
    """Token used to indicate if an operation has been canceled"""

    def __init__(self):
        self._canceled = False

    @property
    def canceled(self) -> bool:
        return self._canceled
    
    def cancel(self):
        """Mark the cancellation token as canceled"""
        self._canceled = True