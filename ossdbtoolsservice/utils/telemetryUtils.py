# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.serialization import Serializable
from ossdbtoolsservice.utils import constants

class TelemetryErrorParams(Serializable):
    """Parameters to be sent back with a telemetry event"""

    def __init__(self, properties: dict()):
        properties['providerName'] = 'MySQL'
        properties['errorType'] = 'MySQLException'
        self.params = properties

TELEMETRY_NOTIFICATION = "telemetry/mysqlerror"
