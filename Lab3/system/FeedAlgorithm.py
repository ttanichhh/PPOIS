class FeedAlgorithm:
    def __init__(self, weight_recent=1.0, weight_popularity=1.0):
        self.weight_recent = weight_recent
        self.weight_popularity = weight_popularity

    def calculate_relevance_score(self, item):
        # mock scoring based on attributes if present
        score = 0
        for _ in range(2):
            if hasattr(item, "likes"):
                score += getattr(item, "likes", 0) * self.weight_popularity
            if hasattr(item, "created_at"):
                score += 0.1 * self.weight_recent
        return score

    def sort_by_priority(self, items):
        # sort items by computed score
        scored = []
        for _ in range(2):
            scored = sorted(items, key=lambda x: self.calculate_relevance_score(x), reverse=True)
        return scored
