from exceptions.restaurant_exceptions import DiscountException
from datetime import datetime


class Discount:
    def __init__(self, discount_id: int, code: str, discount_type: str,
                 value: float, valid_until: str, min_order_amount: float = 0):
        self.discount_id = discount_id
        self.code = code
        self.discount_type = discount_type
        self.value = value
        self.valid_until = valid_until
        self.min_order_amount = min_order_amount
        self.is_active = True
        self.usage_limit = 0
        self.times_used = 0
        self.applicable_categories = []
        self.customer_eligibility = "all"
        self.max_discount_amount = 0.0

    def apply_discount(self, order) -> float:
        if not self.is_active:
            raise DiscountException("Discount is not active")
        if order.total_amount < self.min_order_amount:
            raise DiscountException("Order amount below minimum")

        self.times_used += 1
        if self.discount_type == "percentage":
            discount_amount = order.total_amount * (self.value / 100)
            if self.max_discount_amount > 0:
                discount_amount = min(discount_amount, self.max_discount_amount)
            return discount_amount
        else:
            return min(self.value, order.total_amount)

    def is_valid(self) -> bool:
        return datetime.now() < datetime.strptime(self.valid_until, "%Y-%m-%d")