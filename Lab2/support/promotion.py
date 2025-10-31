from datetime import datetime


class Promotion:
    def __init__(self, promotion_id: int, name: str, description: str,
                 discount_type: str, discount_value: float, start_date: str, end_date: str):
        self.promotion_id = promotion_id
        self.name = name
        self.description = description
        self.discount_type = discount_type
        self.discount_value = discount_value
        self.start_date = start_date
        self.end_date = end_date
        self.is_active = True
        self.applicable_items = []
        self.min_order_amount = 0.0
        self.usage_limit = 0
        self.times_used = 0
        self.promotion_code = ""

    def is_valid(self) -> bool:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return self.start_date <= current_date <= self.end_date and self.is_active

    def apply_promotion(self, order) -> float:
        if not self.is_valid():
            return 0.0

        self.times_used += 1
        if self.discount_type == "percentage":
            return order.total_amount * (self.discount_value / 100)
        else:
            return min(self.discount_value, order.total_amount)