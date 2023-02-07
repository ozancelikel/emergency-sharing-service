class ElasticSearchService:
    def __init__(self, ip, port, index) -> None:
        self.ip = ip
        self.port = port
        self.index = index

    def get_es_result(query):
        return f"ES query result : {query}"