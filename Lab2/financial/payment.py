from support.payment import Payment
from exceptions.restaurant_exceptions import PaymentException


class PaymentProcessor:
    def __init__(self):
        self.processed_payments = []
        self.failed_payments = []
        self.refund_requests = []
        self.payment_methods = ["credit_card", "debit_card", "cash", "digital_wallet"]
        self.processing_fees = {"credit_card": 0.03, "debit_card": 0.01, "digital_wallet": 0.02}

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

    def calculate_processing_fee(self, payment: Payment) -> float:
        fee_percentage = self.processing_fees.get(payment.payment_method, 0.02)
        return payment.amount * fee_percentage

    def process_refund(self, payment: Payment, refund_amount: float) -> bool:
        try:
            if refund_amount > payment.amount:
                raise PaymentException("Refund amount exceeds original payment")

            payment.status = "refunded"
            self.refund_requests.append({
                "original_payment": payment,
                "refund_amount": refund_amount
            })
            return True
        except PaymentException:
            return False

    def get_daily_summary(self, date: str) -> dict:
        total_amount = sum(p.amount for p in self.processed_payments)
        total_fees = sum(self.calculate_processing_fee(p) for p in self.processed_payments)

        return {
            "date": date,
            "total_transactions": len(self.processed_payments),
            "total_amount": total_amount,
            "total_fees": total_fees,
            "net_amount": total_amount - total_fees
        }