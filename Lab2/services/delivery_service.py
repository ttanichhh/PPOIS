from support.delivery import Delivery
from core.employee import Employee
from exceptions.restaurant_exceptions import DeliveryException

class DeliveryService:
    def __init__(self):
        self.active_deliveries = []
        self.completed_deliveries = []
        self.delivery_personnel = []

    def schedule_delivery(self, delivery: Delivery):
        self.active_deliveries.append(delivery)

    @staticmethod
    def calculate_delivery_fee(order_amount: float) -> float:
        if order_amount >= 30.0:
            return 0.0
        return 5.0

    def update_delivery_status(self, delivery: Delivery, new_status: str):
        delivery.status = new_status
        if new_status == "delivered":
            self.active_deliveries.remove(delivery)
            self.completed_deliveries.append(delivery)