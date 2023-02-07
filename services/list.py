from typing import Optional

from services.es_service import ElasticSearchService

class ListService:
    def __init__(self, es_service) -> None:
        self.es_service = es_service

    def get_list(self):
        return ""

    def get_filtered_list(self, pn: int =1, ps: int =1, filter: Optional[dict] = None):
        return ""