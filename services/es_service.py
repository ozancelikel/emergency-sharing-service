class ElasticSearchService:
    def __init__(self, ip, port, index) -> None:
        self.ip = ip
        self.port = port
        self.index = index

    @staticmethod
    def get_es_result(query):
        return f"ES query result : {query}"

    @staticmethod
    def scroll(es, index: str, body, scroll: str, size: int, **kwargs):
        page = es.search(index=index, body=body, scroll=scroll, size=size, **kwargs)
        scroll_id = page['_scroll_id']
        hits = page['hits']['hits']
        while len(hits):
            yield hits
            page = es.scroll(scroll_id=scroll_id, scroll=scroll)
            scroll_id = page['_scroll_id']
            hits = page['hits']['hits']


def example_usage():
    es = ElasticSearchService("localhost", 9200, "test")
    query = {"query": {"match_all": {}}}
    for hits in es.scroll(es, es.index, query, scroll='2m', size=100):
        print(json.dumps(hits, indent=2))