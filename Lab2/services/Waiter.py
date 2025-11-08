from entities.Order import Order
from entities.Customer import Customer


class Waiter:
    def __init__(self, waiter_id, name):
        self.waiter_id = waiter_id
        self.name = name
        self.section = ""
        self.tables = []

    def take_order(self, customer, items):
        unavailable_items = [item for item in items if not item.is_available]
        if unavailable_items:
            unavailable_names = [item.name for item in unavailable_items]
            return f"Cannot take order - unavailable items: {', '.join(unavailable_names)}"

        order_id = f"ORD{len(self.tables) + 1:03d}"
        new_order = Order(order_id, customer)

        for item in items:
            new_order.add_item(item)

        self.tables.append(new_order)

        order_summary = f"Order {order_id} taken from {customer.name}\n"
        order_summary += f"Items: {len(items)}\n"
        order_summary += f"Total: ${new_order.total_amount:.2f}\n"
        order_summary += f"Waiter: {self.name} (Section: {self.section})"
        return order_summary

    def serve_order(self, order):
        if order.status != "completed":
            return f"Order {order.order_id} not ready for serving"

        serving_steps = [
            "Verify order completeness",
            "Check food temperature",
            "Ensure proper presentation",
            "Deliver to customer table",
            "Confirm customer satisfaction"
        ]

        service_report = f"Serving Order {order.order_id}\n"
        for step in serving_steps:
            service_report += f"→ {step}\n"
        service_report += "Order successfully served"
        return service_report