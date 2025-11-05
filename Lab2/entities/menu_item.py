class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = ""
        self.is_available = True

    def apply_discount(self, discount_percent):
        self.price *= (1 - discount_percent / 100)
        return self.price

    def get_item_info(self):
        return f"{self.name} - ${self.price:.2f}"