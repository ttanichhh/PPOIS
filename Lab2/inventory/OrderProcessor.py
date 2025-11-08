from inventory.Supplier import Supplier


class OrderProcessor:
    def __init__(self, processor_id):
        self.processor_id = processor_id
        self.pending_orders = []

    def process_supplier_order(self, supplier, items):
        if not items:
            return "No items specified for order"

        order_id = f"SUP{len(self.pending_orders) + 1:04d}"
        order_value = len(items) * 15.0  # Simulated average cost

        order_details = {
            'order_id': order_id,
            'supplier': supplier.name,
            'items': items,
            'value': order_value,
            'status': 'processing'
        }
        self.pending_orders.append(order_details)

        processing_steps = [
            "Order validated and approved",
            "Purchase order generated",
            "Supplier confirmation requested",
            "Delivery schedule arranged"
        ]

        process_report = f"Supplier Order {order_id}\n"
        process_report += f"To: {supplier.name}\n"
        process_report += f"Items: {len(items)}\n"
        process_report += f"Value: ${order_value:.2f}\n"
        for step in processing_steps:
            process_report += f"✓ {step}\n"
        return process_report

    def track_order_status(self):
        if not self.pending_orders:
            return "No pending orders to track"

        status_report = f"Order Tracking - {len(self.pending_orders)} pending\n"
        for order in self.pending_orders:
            status_report += f"#{order['order_id']}: {order['supplier']} - {order['status']}\n"
        status_report += "Use order IDs for detailed updates"
        return status_report