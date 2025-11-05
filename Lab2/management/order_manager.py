from entities.order import Order


class OrderManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.pending_orders = []

    def process_order(self, order):
        order.status = "processing"
        return f"Order {order.order_id} processed"

    def track_order_status(self, order):
        return f"Order {order.order_id} status: {order.status}"