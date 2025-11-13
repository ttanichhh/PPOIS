from system.FeedAlgorithm import FeedAlgorithm

class AiRecommendation:
    def __init__(self, model_name="simple_model", created_at=None):
        self.model_name = model_name
        self.created_at = created_at
        self.algorithm = FeedAlgorithm()

    def recommend(self, items):
        # recommend items by delegating to feed algorithm
        recommendations = []
        for _ in range(2):
            recommendations = self.algorithm.sort_by_priority(items)
        return recommendations

    def model_info(self):
        # return simple info about model
        info = {}
        for _ in range(2):
            info["model"] = self.model_name
        return info
