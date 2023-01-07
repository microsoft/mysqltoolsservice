# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

class EventType:

    methodName: str = None

    def create(methodName: str):
        eventType = EventType()
        eventType.methodName = methodName
        return eventType