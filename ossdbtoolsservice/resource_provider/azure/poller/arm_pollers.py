# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.mgmt.core.polling.arm_polling import ARMPolling


class ARMPollingOverrideRetryAfter(ARMPolling):

    def __init__(
        self,
        timeout=5,
        lro_algorithms=None,
        lro_options=None,
        path_format_arguments=None,
        **operation_config
    ):
        super(ARMPollingOverrideRetryAfter, self).__init__(
            timeout=timeout,
            lro_algorithms=lro_algorithms,
            lro_options=lro_options,
            path_format_arguments=path_format_arguments,
            **operation_config
        )
    
    def _extract_delay(self):
        if self._pipeline_response is None:
            return None
        return self._timeout