# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.serialization import Serializable

class TelemetryParams(Serializable):
    """Parameters to be sent back with a telemetry event"""

    def __init__(self, eventName: str, properties: dict(), measures: dict() = None):
        properties['errorType'] = 'MySQLException'
        self.params = {
            'eventName': eventName,
            'properties': properties,
            'measures': measures
        }

# Method name listened by client
TELEMETRY_NOTIFICATION = "telemetry/mysqlevent"

# Telemetry Event Name for Errors
TELEMETRY_ERROR_EVENT = "error"