from entities.Order import Order


class OrderManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.pending_orders = []
        self.completed_orders = []

    def process_order(self, order):
        if order.status == "processing":
            return f"Order {order.order_id} is already being processed"

        order.status = "processing"
        self.pending_orders.append(order)

        process_steps = [
            "Order received and verified",
            "Kitchen notified",
            "Preparation in progress"
        ]

        status_report = f"Order {order.order_id} processing started\n"
        for step in process_steps:
            status_report += f"✓ {step}\n"
        return status_report

    def track_order_status(self, order):
        status_messages = {
            "pending": "Waiting to be processed",
            "processing": "Being prepared in kitchen",
            "completed": "Ready for serving",
            "cancelled": "Order was cancelled"
        }

        status_info = f"Order #{order.order_id} Status\n"
        status_info += f"Customer: {order.customer.name}\n"
        status_info += f"Status: {order.status}\n"
        status_info += f"Details: {status_messages.get(order.status, 'Unknown status')}\n"
        status_info += f"Items: {len(order.items)}"
        return status_info