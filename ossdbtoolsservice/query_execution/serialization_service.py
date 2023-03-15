from ossdbtoolsservice.hosting.service_provider import ServiceProvider

class SerializationService(object):
    def __init__(self) -> None:
        self._service_provider: ServiceProvider = None
        self._inprogress_serialization = []
        self._service_action_mapping: dict = {
            SERIALIZE_START_REQUEST: self._handle_get_charsets_request,
            GET_COLLATIONS_REQUEST: self._handle_get_collations_request,
            CREATE_DATABASE_REQUEST: self._handle_create_database_request
        }

    def register(self):
        self._service_provider