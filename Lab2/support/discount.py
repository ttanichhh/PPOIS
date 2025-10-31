from exceptions.restaurant_exceptions import DiscountException


class Discount:
    def __init__(self, discount_id: int, code: str, discount_type: str, value: float):
        self.discount_id = discount_id
        self.code = code
        self.discount_type = discount_type
        self.value = value
        self.is_active = True

    def apply_discount(self, order) -> float:
        if not self.is_active:
            raise DiscountException("Discount is not active")

        if self.discount_type == "percentage":
            return order.total_amount * (self.value / 100)
        else:
            return min(self.value, order.total_amount)