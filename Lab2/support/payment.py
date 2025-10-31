from exceptions.restaurant_exceptions import PaymentException

class Payment:
    def __init__(self, payment_id: int, order, amount: float, payment_method: str):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.payment_method = payment_method
        self.status = "pending"

    def process_payment(self):
        if self.amount <= 0:
            raise PaymentException("Invalid payment amount")
        self.status = "completed"