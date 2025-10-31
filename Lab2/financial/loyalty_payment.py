from financial.payment import Payment, PaymentProcessor
from core.customer import Customer
from utils.loyalty import LoyaltyManager
from exceptions.restaurant_exceptions import LoyaltyException, PaymentException

class LoyaltyPayment:
    def __init__(self, loyalty_manager: LoyaltyManager, payment_processor: PaymentProcessor):
        self.loyalty_manager = loyalty_manager
        self.payment_processor = payment_processor
        self.points_to_cash_ratio = 0.01
        self.conversion_history = []

    def convert_points_to_payment(self, customer: Customer, points_to_convert: int) -> Payment:
        if points_to_convert < 100:
            raise LoyaltyException("Минимальное количество баллов для конвертации: 100")

        available_points = self.loyalty_manager.get_customer_points(customer.customer_id)
        if points_to_convert > available_points:
            raise LoyaltyException("Недостаточно баллов для конвертации")

        payment_amount = points_to_convert * self.points_to_cash_ratio

        loyalty_payment = Payment(
            payment_id=len(self.conversion_history) + 1000,
            order=None,
            amount=payment_amount,
            payment_method="loyalty_points"
        )
        loyalty_payment.status = "completed"

        self.loyalty_manager.deduct_points(customer.customer_id, points_to_convert)

        conversion_record = {
            "customer_id": customer.customer_id,
            "points_converted": points_to_convert,
            "amount_received": payment_amount
        }
        self.conversion_history.append(conversion_record)

        return loyalty_payment

    def split_payment_loyalty_cash(self, customer: Customer, total_amount: float, points_to_use: int) -> tuple:
        available_points = self.loyalty_manager.get_customer_points(customer.customer_id)

        if points_to_use > available_points:
            raise LoyaltyException("Недостаточно баллов для оплаты")

        loyalty_amount = points_to_use * self.points_to_cash_ratio
        cash_amount = total_amount - loyalty_amount

        if cash_amount < 0:
            raise LoyaltyException("Сумма баллов превышает общую сумму")

        loyalty_payment = self.convert_points_to_payment(customer, points_to_use)

        cash_payment = Payment(
            payment_id=len(self.conversion_history) + 2000,
            order=None,
            amount=cash_amount,
            payment_method="cash"
        )

        return loyalty_payment, cash_payment