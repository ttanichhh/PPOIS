from entities.order import Order
from entities.customer import Customer


class Waiter:
    def __init__(self, waiter_id, name):
        self.waiter_id = waiter_id
        self.name = name
        self.section = ""
        self.tables = []

    def take_order(self, customer, items):
        new_order = Order(f"ORD{len(self.tables) + 1}", customer)
        for item in items:
            new_order.add_item(item)
        return new_order

    def serve_order(self, order):
        return f"Serving order {order.order_id}"