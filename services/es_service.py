from elasticsearch import Elasticsearch
from flask import json

from models.request.listing_request import ListingRequest


class ElasticSearchService:
    def __init__(self, ip, port, index) -> None:
        self.ip = ip
        self.port = port
        self.index = index
        self.url = f"http://{self.ip}:{self.port}"
        self.es = Elasticsearch([self.url])
    
    def get_es_result(self, query):
        return self.create_list_es_query(query)

    def add_new_entry(self, data):
        request = ListingRequest(**data).to_dict()
        self.es.index(index=self.index, doc_type="_doc", query=request)
        return "OK"

    @staticmethod
    def _get_filter_query(filter_data):
        query = {
            "match_all": {}
        }

        if filter_data:
            query = {
                "match": {
                    "title": f'{filter_data}'
                }
            }
        return query

    def create_list_es_query(self, filter_data):
        query = self._get_filter_query(filter_data)
        page = self.es.search(index=self.index, query=query)
        return json.dumps(page['hits']['hits'], indent=4)

    def scroll(self, filter_data, page_number, page_size):
        query = self._get_filter_query(filter_data)
        page = self.es.search(index=self.index, query=query, from_=page_number, size=page_size)
        hits = page['hits']['hits']
        return json.dumps(hits, indent=4)
