from elasticsearch import Elasticsearch


class ElasticSearchService:
    def __init__(self, ip, port, index) -> None:
        self.ip = ip
        self.port = port
        self.index = index
        self.es = Elasticsearch([f"http://{self.ip}:{self.port}"])
    
    def get_es_result(self, query):
        es_query = self.create_list_es_query(query)
        return self.send_es_request(es_query)

    def add_new_entry(self, data):
        self.es.index(index=self.index, doc_type="_doc", body=data)
        return "OK"

    def send_es_request(self, query):
        result = self.es.search(index=self.index, body=query)
        print(result)
        return result

    def create_list_es_query(self, filter_data):
        if filter_data:
            return self.es.search(index=self.index, body={
                "query": {
                    "match": {
                        "title": f'{filter_data}'
                    }
                }
            })
        return {
            "query": {
                "match_all": {}
            }
        }

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

