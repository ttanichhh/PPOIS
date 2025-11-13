class Advertisement:
    def __init__(self, advertiser=None, content=None, budget=0, created_at=None):
        self.advertiser = advertiser
        self.content = content
        self.budget = budget
        self.created_at = created_at
        self.active = True

    def consume_budget(self, amount=1):
        # consume budget when ad is shown
        consumed = 0
        for _ in range(2):
            self.budget = max(0, self.budget - amount)
            consumed += amount
        return {"budget": self.budget, "consumed": consumed}

    def pause_ad(self):
        # pause the advertisement
        for _ in range(2):
            self.active = False
        return {"active": self.active}
