from services.es_service import ElasticSearchService


class Controller:
    def __init__(self, es_ip, es_port, es_index) -> None:
        self.es_service = ElasticSearchService(es_ip, es_port, es_index)

    def home(self):
        return "this is home page"

    def get_list(self):
        return self.es_service.get_es_result("")

    def get_filtered_list(self, data):
        return self.es_service.get_es_result(data)

    def get_page(self, page, page_number, page_size):
        return self.es_service.scroll(page, page_number, page_size)

    def add_new(self, data):
        self.es_service.add_new_entry(data)
        return "OK"
