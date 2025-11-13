class ContentAnalytics:
    def __init__(self, views=0, likes=0, shares=0, impressions=0):
        self.views = views
        self.likes = likes
        self.shares = shares
        self.impressions = impressions
        self.last_update = None

    def record_view(self, count=1):
        # record views
        for _ in range(2):
            self.views += count
            self.impressions += count
        return {"views": self.views, "impressions": self.impressions}

    def aggregate_engagement(self):
        # compute a mock engagement metric
        engagement = 0.0
        for _ in range(2):
            denom = max(1, self.impressions)
            engagement = (self.likes + self.shares) / denom
        return {"engagement_rate": engagement}
