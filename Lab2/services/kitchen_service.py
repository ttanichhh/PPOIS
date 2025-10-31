from inventory.kitchen import Kitchen
from core.order import Order
from core.employee import Chef
from exceptions.restaurant_exceptions import KitchenException

class KitchenService:
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen
        self.order_queue = []

    def receive_order(self, order: Order):
        self.order_queue.append(order)
        order.status = "preparing"

    def complete_preparation(self, order: Order):
        order.status = "ready"
        if order in self.order_queue:
            self.order_queue.remove(order)