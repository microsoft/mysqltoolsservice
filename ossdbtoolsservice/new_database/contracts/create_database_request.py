# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ossdbtoolsservice.hosting import IncomingMessageConfiguration
from ossdbtoolsservice.serialization import Serializable


class CreateDatabaseRequest(Serializable):

    def __init__(self):
        self.owner_uri: str = None
        self.db_name: str = None
        self.charset: str = None
        self.collation: str = None


CREATE_DATABASE_REQUEST = IncomingMessageConfiguration('mysqlnewdatabase/create', CreateDatabaseRequest)