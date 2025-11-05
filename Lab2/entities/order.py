from entities.customer import Customer
from entities.menu_item import MenuItem


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.total_amount = 0.0
        self.status = "pending"

    def add_item(self, item):
        self.items.append(item)
        self.total_amount += item.price

    def calculate_total(self):
        self.total_amount = sum(item.price for item in self.items)
        return self.total_amount

    def get_order_summary(self):
        return f"Order #{self.order_id} - Total: ${self.total_amount:.2f}"