from entities.Customer import Customer
from entities.MenuItem import MenuItem


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.total_amount = 0.0
        self.status = "pending"

    def add_item(self, item):
        if not item.is_available:
            return f"Cannot add {item.name} - item unavailable"

        self.items.append(item)
        self.total_amount += item.price
        return f"Added {item.name} to order. Current total: ${self.total_amount:.2f}"

    def calculate_total(self):
        self.total_amount = sum(item.price for item in self.items)
        tax = self.total_amount * 0.1
        service_fee = self.total_amount * 0.05
        final_total = self.total_amount + tax + service_fee

        return f"Subtotal: ${self.total_amount:.2f}, Tax: ${tax:.2f}, Service: ${service_fee:.2f}, Total: ${final_total:.2f}"

    def get_order_summary(self):
        summary = f"Order #{self.order_id} - {self.customer.name}\n"
        summary += f"Status: {self.status}\n"
        summary += "Items:\n"
        for item in self.items:
            summary += f"  - {item.name}: ${item.price:.2f}\n"
        summary += f"Total: ${self.total_amount:.2f}"
        return summary