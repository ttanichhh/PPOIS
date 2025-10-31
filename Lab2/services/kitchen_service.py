from inventory.kitchen import Kitchen
from core.order import Order, OrderItem
from core.employee import Chef
from exceptions.restaurant_exceptions import KitchenException

class KitchenService:
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen
        self.order_queue = []
        self.preparation_times = {}
        self.quality_controls = []
        self.waste_records = []
        self.equipment_maintenance = []

    def receive_order(self, order: Order):
        self.order_queue.append(order)
        self.assign_to_chef(order)

    def assign_to_chef(self, order: Order):
        available_chefs = [chef for chef in self.kitchen.chefs if len(chef.current_orders) < 3]

        if not available_chefs:
            raise KitchenException("No available chefs to handle the order")

        assigned_chef = min(available_chefs, key=lambda x: len(x.current_orders))
        assigned_chef.current_orders.append(order)
        self.kitchen.assign_order(order, assigned_chef)

    @staticmethod
    def start_preparation(order: Order):
        for order_item in order.order_items:
            order_item.start_cooking()

        order.status = "preparing"

    def complete_preparation(self, order: Order):
        for order_item in order.order_items:
            order_item.finish_cooking()

        order.status = "ready"

        # Remove from chefs' current orders
        for chef in self.kitchen.chefs:
            if order in chef.current_orders:
                chef.current_orders.remove(order)

    def get_estimated_wait_time(self, order: Order) -> int:
        total_time = 0
        for item in order.order_items:
            total_time += item.menu_item.preparation_time * item.quantity

        # Add queue time
        queue_position = self.order_queue.index(order) if order in self.order_queue else 0
        queue_time = queue_position * 5  # 5 minutes per order in queue

        return total_time + queue_time

    def record_waste(self, item_name: str, quantity: int, reason: str):
        waste_record = {
            "item_name": item_name,
            "quantity": quantity,
            "reason": reason,
            "recorded_at": "2024-01-20 12:00:00",
            "cost": 0.0  # This would be calculated based on item cost
        }
        self.waste_records.append(waste_record)

    def perform_quality_check(self, order: Order, rating: int, comments: str):
        quality_check = {
            "order_id": order.order_id,
            "rating": rating,
            "comments": comments,
            "checked_by": "Quality Manager",
            "check_time": "2024-01-20 12:00:00"
        }
        self.quality_controls.append(quality_check)

    def get_kitchen_performance(self) -> dict:
        completed_orders = [order for order in self.kitchen.current_orders if order.status == "ready"]
        avg_preparation_time = 25.0  # This would be calculated

        return {
            "orders_in_progress": len(self.kitchen.current_orders),
            "orders_completed_today": len(completed_orders),
            "average_preparation_time": avg_preparation_time,
            "chef_utilization": len(self.kitchen.chefs) / 10.0,  # Assuming 10 is max
            "quality_rating": 4.5
        }