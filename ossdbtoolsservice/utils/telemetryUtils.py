# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.utils.eventType import EventType

class TelemetryParams:
    """Parameters to be sent back with a telemetry event"""

    def __init__(self, eventName: str, properties: dict(), measures: dict()):
        self.eventName = eventName
        self.properties = properties
        self.measures = measures   

class TelemetryNotification:
    type = EventType.create("telemetry/mysqlevent")


TELEMETRY_NOTIFICATION = 'telemetry/mysqlevent'