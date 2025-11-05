from entities.order import Order


class Payment:
    def __init__(self, payment_id, order):
        self.payment_id = payment_id
        self.order = order
        self.amount = order.total_amount
        self.method = "cash"
        self.status = "pending"

    def process_payment(self):
        self.status = "completed"
        return True

    def get_payment_details(self):
        return f"Payment #{self.payment_id} - ${self.amount:.2f}"