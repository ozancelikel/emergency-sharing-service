import aiohttp

class ElasticSearchService:
    def __init__(self, ip, port, index) -> None:
        self.ip = ip
        self.port = port
        self.index = index
        self.client = aiohttp.ClientSession()
    
    def get_es_result(self, query, filter=None):
        es_query = self.create_es_query(query, filter)
        # RUN send_es_request(es_query)
        return f"ES query result : {query}"

    def send_es_request(self, query):
        resp = self.client.post(
            headers=f"http://{self.ip}:{self.port}/{self.index}",
            data=query
        )

        return resp.data

    @staticmethod
    def create_list_es_query(query, filter):
        if filter:
            return "filtered list query"
        return "unfiltered list query"

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



