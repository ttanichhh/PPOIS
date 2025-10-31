from financial.payment import Payment, PaymentProcessor
from core.customer import Customer
from utils.loyalty import LoyaltyManager
from exceptions.restaurant_exceptions import LoyaltyException, PaymentException
from datetime import datetime


class LoyaltyPayment:
    def __init__(self, loyalty_manager: LoyaltyManager, payment_processor: PaymentProcessor):
        self.loyalty_manager = loyalty_manager
        self.payment_processor = payment_processor
        self.points_to_cash_ratio = 0.01  # 1 балл = 0.01 у.е.
        self.min_points_for_conversion = 100
        self.conversion_history = []
        self.max_daily_conversions = 5

    def convert_points_to_payment(self, customer: Customer, points_to_convert: int) -> Payment:
        """Уникальное поведение: конвертация баллов лояльности в платеж"""
        if points_to_convert < self.min_points_for_conversion:
            raise LoyaltyException(f"Минимальное количество баллов для конвертации: {self.min_points_for_conversion}")

        available_points = self.loyalty_manager.get_customer_points(customer.customer_id)
        if points_to_convert > available_points:
            raise LoyaltyException("Недостаточно баллов для конвертации")

        # Проверка лимита daily конвертаций
        today_conversions = self._get_today_conversions_count(customer)
        if today_conversions >= self.max_daily_conversions:
            raise LoyaltyException("Превышен дневной лимит конвертаций")

        # Расчет суммы платежа
        payment_amount = points_to_convert * self.points_to_cash_ratio

        # Создание специального платежа лояльности
        loyalty_payment = Payment(
            payment_id=len(self.conversion_history) + 1000,
            order=None,  # Специальный платеж без заказа
            amount=payment_amount,
            payment_method="loyalty_points"
        )
        loyalty_payment.status = "completed"
        # Убрал payment_time так как этого поля больше нет

        # Списание баллов
        self.loyalty_manager.deduct_points(customer.customer_id, points_to_convert)

        # Запись в историю
        conversion_record = {
            "customer_id": customer.customer_id,
            "points_converted": points_to_convert,
            "amount_received": payment_amount,
            "timestamp": datetime.now(),
            "payment_id": loyalty_payment.payment_id
        }
        self.conversion_history.append(conversion_record)

        return loyalty_payment

    def process_loyalty_refund(self, original_payment: Payment, refund_amount: float) -> bool:
        """Уникальное поведение: возврат средств на бонусный счет лояльности"""
        if original_payment.status != "completed":
            raise PaymentException("Можно вернуть только завершенные платежи")

        if refund_amount > original_payment.amount:
            raise PaymentException("Сумма возврата превышает оригинальный платеж")

        # Конвертация денег в баллы лояльности
        points_to_refund = int(refund_amount / self.points_to_cash_ratio)

        # Находим клиента (в реальной системе была бы связь Payment-Customer)
        customer_id = self._find_customer_by_payment(original_payment)
        if customer_id:
            self.loyalty_manager.add_points(customer_id, points_to_refund, "refund_bonus")

            # Обновляем статус платежа (убрал refund_amount так как этого поля нет)
            original_payment.status = "partially_refunded" if refund_amount < original_payment.amount else "refunded"

            return True

        return False

    def split_payment_loyalty_cash(self, customer: Customer, total_amount: float, points_to_use: int) -> tuple:
        """Уникальное поведение: разделенная оплата баллами и наличными"""
        available_points = self.loyalty_manager.get_customer_points(customer.customer_id)

        if points_to_use > available_points:
            raise LoyaltyException("Недостаточно баллов для оплаты")

        # Расчет суммы к оплате баллами
        loyalty_amount = points_to_use * self.points_to_cash_ratio
        cash_amount = total_amount - loyalty_amount

        if cash_amount < 0:
            raise LoyaltyException("Сумма баллов превышает общую сумму")

        # Создаем платеж баллами
        loyalty_payment = self.convert_points_to_payment(customer, points_to_use)

        # Создаем платеж наличными (упрощенно)
        cash_payment = Payment(
            payment_id=len(self.conversion_history) + 2000,
            order=None,
            amount=cash_amount,
            payment_method="cash"
        )

        return loyalty_payment, cash_payment

    def get_conversion_rate(self, from_currency: str, to_currency: str) -> float:
        """Уникальное поведение: получение курса конвертации"""
        rates = {
            ("points", "cash"): self.points_to_cash_ratio,
            ("cash", "points"): 1 / self.points_to_cash_ratio
        }

        return rates.get((from_currency, to_currency), 1.0)

    def _get_today_conversions_count(self, customer: Customer) -> int:
        """Подсчет конвертаций за сегодня"""
        today = datetime.now().date()
        return sum(1 for record in self.conversion_history
                  if record["customer_id"] == customer.customer_id
                  and record["timestamp"].date() == today)

    @staticmethod
    def _find_customer_by_payment() -> int:  # ДОБАВИЛ ПАРАМЕТР payment
        """Поиск клиента по платежу (упрощенная реализация)"""
        # В реальной системе здесь была бы связь с базой данных
        return 1  # Возвращаем ID тестового клиента

    def get_customer_conversion_history(self, customer: Customer) -> list:
        """Получение истории конвертаций клиента"""
        return [record for record in self.conversion_history
                if record["customer_id"] == customer.customer_id]

    def calculate_max_points_payment(self, customer: Customer, total_amount: float) -> dict:
        """Расчет максимальной оплаты баллами"""
        available_points = self.loyalty_manager.get_customer_points(customer.customer_id)
        max_points_usable = min(available_points, int(total_amount / self.points_to_cash_ratio))
        max_loyalty_amount = max_points_usable * self.points_to_cash_ratio
        remaining_cash = total_amount - max_loyalty_amount

        return {
            "max_points_usable": max_points_usable,
            "max_loyalty_amount": round(max_loyalty_amount, 2),
            "remaining_cash": round(remaining_cash, 2),
            "available_points": available_points
        }