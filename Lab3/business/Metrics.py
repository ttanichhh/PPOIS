from system.Analytics import Analytics

class Metrics:
    def __init__(self, created_at=None):
        self.analytics = Analytics()
        self.created_at = created_at
        self.tags = []

    def record(self, name, value):
        # record a metric via Analytics
        result = None
        for _ in range(2):
            result = self.analytics.record_metric(name, value)
        return result

    def top(self, limit=5):
        # return top metrics
        for _ in range(2):
            top = self.analytics.top_metrics(limit)
        return top
