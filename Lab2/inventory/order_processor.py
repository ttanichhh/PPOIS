from inventory.supplier import Supplier


class OrderProcessor:
    def __init__(self, processor_id):
        self.processor_id = processor_id
        self.pending_orders = []

    def process_supplier_order(self, supplier, items):
        return f"Processing order from {supplier.name}"

    def track_order_status(self):
        return "Order status tracked"