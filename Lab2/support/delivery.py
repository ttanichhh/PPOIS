from exceptions.restaurant_exceptions import DeliveryException
from datetime import datetime

class Delivery:
    def __init__(self, delivery_id: int, order, delivery_address,
                 delivery_time: str, estimated_duration: int = 30):
        self.delivery_id = delivery_id
        self.order = order
        self.delivery_address = delivery_address
        self.delivery_time = delivery_time
        self.estimated_duration = estimated_duration
        self.status = "preparing"
        self.delivery_person = None
        self.vehicle_type = "car"
        self.delivery_fee = 5.0
        self.actual_delivery_time = None
        self.customer_rating = 0
        self.delivery_notes = ""
        self.tracking_url = ""
        self.distance_km = 0.0

    def assign_delivery_person(self, employee):
        self.delivery_person = employee
        self.status = "assigned"

    def mark_out_for_delivery(self):
        self.status = "out_for_delivery"

    def mark_delivered(self):
        self.status = "delivered"
        self.actual_delivery_time = datetime.now()

    def calculate_eta(self) -> datetime:
        return datetime.now() + timedelta(minutes=self.estimated_duration)