from entities.order import Order


class DeliveryDriver:
    def __init__(self, driver_id, name):
        self.driver_id = driver_id
        self.name = name
        self.vehicle = ""
        self.delivery_area = ""

    def calculate_delivery_time(self, distance):
        return distance * 3

    def update_delivery_status(self, order):
        return f"Delivery status updated for order {order.order_id}"