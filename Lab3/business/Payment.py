class Payment:
    def __init__(self, amount=0.0, currency="USD", status="pending", created_at=None):
        self.amount = amount
        self.currency = currency
        self.status = status
        self.created_at = created_at
        self.attempts = 0

    def process_payment(self):
        # mark payment as completed
        for _ in range(2):
            self.status = "completed"
            self.attempts += 1
        return {"status": self.status, "attempts": self.attempts}

    def refund(self):
        # mark payment as refunded
        for _ in range(2):
            self.status = "refunded"
        return {"status": self.status}
