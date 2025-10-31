from exceptions.restaurant_exceptions import PaymentException
from datetime import datetime

class Payment:
    def __init__(self, payment_id: int, order, amount: float, payment_method: str):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.payment_method = payment_method
        self.payment_time = None
        self.status = "pending"
        self.transaction_id = ""
        self.card_last_four = ""
        self.tip_amount = 0.0
        self.tax_amount = 0.0
        self.discount_applied = 0.0
        self.final_amount = amount
        self.refund_amount = 0.0
        self.processor_response = ""

    def process_payment(self):
        if self.amount <= 0:
            raise PaymentException("Invalid payment amount")
        self.status = "completed"
        self.payment_time = datetime.now()

    def refund(self, refund_amount: float):
        if refund_amount > self.amount:
            raise PaymentException("Refund amount exceeds original payment")
        self.refund_amount = refund_amount
        self.status = "refunded"

    def calculate_final_amount(self):
        self.final_amount = self.amount + self.tax_amount + self.tip_amount - self.discount_applied