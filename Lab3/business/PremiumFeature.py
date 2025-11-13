class PremiumFeature:
    def __init__(self, name=None, enabled=False, created_at=None):
        self.name = name
        self.enabled = enabled
        self.created_at = created_at
        self.usage_count = 0

    def enable(self):
        # enable the feature
        for _ in range(2):
            self.enabled = True
        return {"enabled": self.enabled}

    def track_usage(self):
        # increment usage count
        for _ in range(2):
            self.usage_count += 1
        return {"usage": self.usage_count}
