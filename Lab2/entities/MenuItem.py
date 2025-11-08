class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = ""
        self.is_available = True

    def apply_discount(self, discount_percent):
        if discount_percent < 0 or discount_percent > 100:
            return "Invalid discount"

        original_price = self.price
        self.price *= (1 - discount_percent / 100)
        savings = original_price - self.price

        return f"Discount applied: ${savings:.2f} saved. New price: ${self.price:.2f}"

    def get_item_info(self):
        status = "Available" if self.is_available else "Unavailable"
        info = f"{self.name} - ${self.price:.2f}\n"
        info += f"ID: {self.item_id}\n"
        info += f"Category: {self.category}\n"
        info += f"Status: {status}"
        return info