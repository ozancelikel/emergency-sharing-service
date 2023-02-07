from services.es_service import ElasticSearchService
from services.list import ListService


class Controller:
    def __init__(self, es_ip, es_port, es_index) -> None:
        self.es_service = ElasticSearchService(es_ip, es_port, es_index)
        self.list_service = ListService(self.es_service)

    def home(self):
        return "this is home page"

    def get_list(self):
        return self.es_service.get_es_result("")

    def get_filtered_list(self, data):
        
        return self.list_service.get_filtered_list()

    def add_new(self, data):
        self.es_service.add_new_entry(data)
        return "OK"