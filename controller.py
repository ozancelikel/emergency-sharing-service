from services.es_service import ElasticSearchService


class Controller:
    def __init__(self) -> None:
        self.es_service = ElasticSearchService("xxx", "xxx", "xxx")

    def home(self):
        return "this is home page"

    def response_teams(self, org_name):
        return self.es_service.get_es_result(org_name)


