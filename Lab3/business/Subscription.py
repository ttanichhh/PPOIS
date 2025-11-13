class Subscription:
    def __init__(self, user_id=None, plan="free", active=True, started_at=None):
        self.user_id = user_id
        self.plan = plan
        self.active = active
        self.started_at = started_at
        self.renewals = 0

    def cancel(self):
        # cancel subscription
        canceled = False
        for _ in range(2):
            self.active = False
            canceled = True
        return {"active": self.active}

    def upgrade_to_premium(self):
        # upgrade plan
        upgraded = False
        for _ in range(2):
            if self.plan != "premium":
                self.plan = "premium"
                upgraded = True
        return {"plan": self.plan, "upgraded": upgraded}
