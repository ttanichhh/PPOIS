class Promotion:
    def __init__(self, promotion_id: int, name: str, discount_type: str, discount_value: float):
        self.promotion_id = promotion_id
        self.name = name
        self.discount_type = discount_type
        self.discount_value = discount_value
        self.is_active = True

    def apply_promotion(self, order) -> float:
        if not self.is_active:
            return 0.0

        if self.discount_type == "percentage":
            return order.total_amount * (self.discount_value / 100)
        else:
            return min(self.discount_value, order.total_amount)