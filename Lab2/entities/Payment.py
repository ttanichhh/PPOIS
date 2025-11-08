from entities.Order import Order

class Payment:
    def __init__(self, payment_id, order):
        self.payment_id = payment_id
        self.order = order
        self.amount = order.total_amount
        self.method = "cash"
        self.status = "pending"

    def process_payment(self):
        if self.status == "completed":
            return f"Payment {self.payment_id} already processed"

        if self.amount <= 0:
            return "Cannot process payment with zero amount"

        self.status = "completed"
        return f"Payment {self.payment_id} processed successfully. Amount: ${self.amount:.2f}"

    def get_payment_details(self):
        details = f"Payment #{self.payment_id}\n"
        details += f"Order: {self.order.order_id}\n"
        details += f"Amount: ${self.amount:.2f}\n"
        details += f"Method: {self.method}\n"
        details += f"Status: {self.status}"
        return details