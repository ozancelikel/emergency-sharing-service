from services.es_service import ElasticSearchService
from services.list import ListService


class Controller:
    def __init__(self) -> None:
        self.es_service = ElasticSearchService("xxx", "xxx", "xxx")
        self.list_service = ListService(self.es_service)

    def home(self):
        return "this is home page"

    def get_list(self):
        return self.list_service.get_list()

    def get_filtered_list(self, data):
        return self.list_service.get_filtered_list()


