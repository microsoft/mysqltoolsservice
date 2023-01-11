# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.serialization import Serializable

class TelemetryParams(Serializable):
    """Parameters to be sent back with a telemetry event"""

    def __init__(self, eventName: str, properties: dict(), measures: dict() = None):
        self.params = TelemetryProperties(eventName, properties, measures) 

class TelemetryProperties(Serializable):

    def __init__(self, eventName: str, properties: dict(), measures):
        self.eventName = eventName
        self.properties = properties
        self.measures = measures 

TELEMETRY_NOTIFICATION = "telemetry/mysqlevent"
