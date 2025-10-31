from exceptions.restaurant_exceptions import DeliveryException

class Delivery:
    def __init__(self, delivery_id: int, order, delivery_address, delivery_time: str):
        self.delivery_id = delivery_id
        self.order = order
        self.delivery_address = delivery_address
        self.delivery_time = delivery_time
        self.status = "preparing"
        self.delivery_person = None

    def assign_delivery_person(self, employee):
        self.delivery_person = employee
        self.status = "assigned"

    def mark_delivered(self):
        self.status = "delivered"