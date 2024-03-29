# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
import unittest.mock as mock

from ossdbtoolsservice.connection import ConnectionService
from ossdbtoolsservice.connection.contracts import ConnectionType
from ossdbtoolsservice.metadata import MetadataService
from ossdbtoolsservice.metadata.contracts import (METADATA_LIST_REQUEST,
                                                  MetadataListParameters,
                                                  MetadataListResponse,
                                                  MetadataType, ObjectMetadata)
from ossdbtoolsservice.utils import constants
from tests.mocks.service_provider_mock import ServiceProviderMock
from tests.mysqlsmo_tests.utils import MockMySQLServerConnection
from tests.utils import (
    MockMySQLCursor, MockRequestContext, MockThread)


class TestMetadataService(unittest.TestCase):
    """Methods for testing the metadata service"""

    def setUp(self):
        self.metadata_service = MetadataService()
        self.connection_service = ConnectionService()
        self.service_provider = ServiceProviderMock({
            constants.METADATA_SERVICE_NAME: self.metadata_service,
            constants.CONNECTION_SERVICE_NAME: self.connection_service})
        self.metadata_service.register(self.service_provider)
        self.test_uri = 'test_uri'

    def test_initialization(self):
        """Test that the metadata service registers its handlers correctly"""
        # Verify that the correct request handler was set up via the call to register during test setup
        self.service_provider.server.set_request_handler.assert_called_once_with(
            METADATA_LIST_REQUEST, self.metadata_service._handle_metadata_list_request)

    def test_metadata_list_request_error(self):
        """Test that the proper error response is sent if there is an error while handling a metadata list request"""
        request_context = MockRequestContext()
        params = MetadataListParameters()
        params.owner_uri = self.test_uri
        self.metadata_service._list_metadata = mock.Mock(side_effect=Exception)
        mock_thread = MockThread()
        with mock.patch('threading.Thread', new=mock.Mock(side_effect=mock_thread.initialize_target)):
            # If I call the metadata list request handler and its execution raises an error
            self.metadata_service._handle_metadata_list_request(request_context, params)
        # Then an error response is sent
        self.assertIsNotNone(request_context.last_error_message)
        self.assertIsNone(request_context.last_notification_method)
        self.assertIsNone(request_context.last_response_params)
