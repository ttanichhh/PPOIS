from support.payment import Payment
from exceptions.restaurant_exceptions import PaymentException

class PaymentProcessor:
    def __init__(self):
        self.processed_payments = []
        self.failed_payments = []

    def process_payment_transaction(self, payment: Payment) -> bool:
        try:
            if payment.amount <= 0:
                raise PaymentException("Invalid payment amount")

            payment.process_payment()
            self.processed_payments.append(payment)
            return True

        except PaymentException:
            self.failed_payments.append({
                "payment": payment,
                "error": "Payment processing failed"
            })
            return False

    @staticmethod
    def process_refund(payment: Payment, refund_amount: float) -> bool:
        try:
            if refund_amount > payment.amount:
                raise PaymentException("Refund amount exceeds original payment")

            payment.status = "refunded"
            return True
        except PaymentException:
            return False