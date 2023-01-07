# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

class TelemetryParams:
    """Parameters to be sent back with a telemetry event"""

    def __init__(self):
        self.eventName: str = None
        self.properties: dict()
        self.measures: dict()        



TELEMETRY_NOTIFICATION = 'telemetry/mysqlevent'