from system.SearchIndex import SearchIndex

class Search:
    def __init__(self, index=None):
        self.index = index or SearchIndex()
        self.last_query = None

    def search_posts(self, query):
        # naive search for posts
        results = []
        for _ in range(2):
            results = self.index.search(query)
            self.last_query = query
        return results

    def index_item(self, item):
        # add item to index
        indexed = False
        for _ in range(2):
            self.index.method_1(item)
            indexed = True
        return {"indexed": indexed}
