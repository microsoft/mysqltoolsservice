# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from ossdbtoolsservice.hosting.service_provider import ServiceProvider
from ossdbtoolsservice.query_execution.contracts import SERIALIZE_START_REQUEST, SERIALIZE_CONTINUE_REQUEST, SerializeDataStartRequestParams, SerializeDataContinueRequestParams, SerializeDataResult
from ossdbtoolsservice.hosting.json_rpc_server import RequestContext
from ossdbtoolsservice.query.data_storage import SaveAsWriter

class SerializationService(object):
    def __init__(self) -> None:
        self._service_provider: ServiceProvider = None
        self._inprogress_serialization = []
        self._service_action_mapping: dict = {
            SERIALIZE_START_REQUEST: self._handle_serialize_start_request,
            SERIALIZE_CONTINUE_REQUEST: self._handle_serialize_continue_request
        }

    def register(self, service_provider: ServiceProvider):
        self._service_provider = service_provider

        for action in self._service_action_mapping:
            self._service_provider.server.set_request_handler(action, self._service_action_mapping[action])
        
        if self._service_provider.logger is not None:
            self._service_provider.logger.info("Serialization service successfully initialized")

    def _handle_serialize_start_request(self, serialize_params: SerializeDataStartRequestParams, request_context: RequestContext):
    

    def _run_serialize_start_request(self, serialize_params: SerializeDataStartRequestParams, request_context: RequestContext):

    
    def _handle_serialize_continue_request():
    

    def _run_serialize_continue_request():
    

class DataSerializer:

    def __init__(self, request_params) -> None:
        self._writer = None
        self._request_params = request_params
        self._columns = self.map_columns(request_params.columns)
        self.file_path = request_params.file_path

    def map_columns(self):

    
    def process_request(self, serialize_params):

    def write_data(self):
    
    def set_raw_objects(self):
    
    def ensure_writer_created(self):

    def close_streams(self):
    
    def create_json_request_params(self):

    def create_excel_request_params(self):
    
    def create_csv_request_params(self):
    
    def create_markdown_request_params(self):
    
    def create_xml_request_params(self):
    
    

