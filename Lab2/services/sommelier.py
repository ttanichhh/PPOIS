class Sommelier:
    def __init__(self, sommelier_id, name):
        self.sommelier_id = sommelier_id
        self.name = name
        self.wine_knowledge = ""

    def recommend_wine(self, dish):
        return f"Wine recommendation for {dish.name}"

    def manage_wine_cellar(self):
        return "Wine cellar managed"