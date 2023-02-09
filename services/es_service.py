import requests
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
        # return self.send_es_req(Search().query("match", _id=query)).to_dict()

    # def send_es_req(self, query):
    #     data = json.dumps(query)
    #     res = requests.post(
    #         url=self.url,
    #         headers=self.headers,
    #         data=data
    #     )
    #     es_result = res.text
    #     es_result = json.loads(es_result)
    #     return es_result

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
        return json.dumps(page, indent=4)

    def scroll_test(self, filter_data):
        query = self._get_filter_query(filter_data)
        page = self.es.search(index=self.index, query=query)
        hits = page['hits']['hits']
        while len(hits):
            yield hits
            page = self.es.scroll(scroll_id=page['_scroll_id'], scroll='2m')
            scroll_id = page['_scroll_id']
            hits = page['hits']['hits']

    @staticmethod
    def scroll(self, index: str, body, scroll: str, size: int, **kwargs):
        page = self.es.search(index=index, doc_type="_doc", body=body, scroll=scroll, size=size, **kwargs)
        scroll_id = page['_scroll_id']
        hits = page['hits']['hits']
        while len(hits):
            yield hits
            page = self.es.scroll(scroll_id=scroll_id, scroll=scroll)
            scroll_id = page['_scroll_id']
            hits = page['hits']['hits']
