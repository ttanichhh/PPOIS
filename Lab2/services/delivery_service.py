from support.delivery import Delivery
from core.employee import Employee
from exceptions.restaurant_exceptions import DeliveryException
from datetime import datetime, timedelta


class DeliveryService:
    def __init__(self):
        self.active_deliveries = []
        self.completed_deliveries = []
        self.delivery_personnel = []
        self.delivery_zones = []
        self.vehicle_fleet = []
        self.delivery_metrics = {}
        self.route_optimization = {}

    def schedule_delivery(self, delivery: Delivery):
        if not self.is_delivery_zone_covered(delivery.delivery_address):
            raise DeliveryException("Delivery address not in service area")

        self.active_deliveries.append(delivery)
        self.assign_delivery_person(delivery)

    def assign_delivery_person(self, delivery: Delivery):
        available_personnel = [person for person in self.delivery_personnel
                               if len([d for d in self.active_deliveries
                                       if d.delivery_person == person]) < 3]

        if not available_personnel:
            raise DeliveryException("No available delivery personnel")

        # Assign based on proximity to restaurant
        assigned_person = available_personnel[0]  # Simplified assignment
        delivery.assign_delivery_person(assigned_person)

    @staticmethod
    def is_delivery_zone_covered(address) -> bool:
        # Simplified zone check - in real system, would use geocoding
        covered_cities = ["New York", "Brooklyn", "Queens", "Manhattan"]
        return any(city in address.city for city in covered_cities)

    def update_delivery_status(self, delivery: Delivery, new_status: str):
        delivery.status = new_status

        if new_status == "out_for_delivery":
            delivery.mark_out_for_delivery()
        elif new_status == "delivered":
            delivery.mark_delivered()
            self.active_deliveries.remove(delivery)
            self.completed_deliveries.append(delivery)

    @staticmethod
    def calculate_delivery_fee(distance_km: float, order_amount: float) -> float:
        base_fee = 5.0
        distance_fee = max(0.0, (distance_km - 5.0) * 0.5)  # $0.5 per km after 5km
        free_delivery_threshold = 30.0

        if order_amount >= free_delivery_threshold:
            return 0.0  # 🔹 Вот почему возвращается 0.0!

        return base_fee + distance_fee

    @staticmethod
    def get_delivery_eta(delivery: Delivery) -> datetime:
        if delivery.status == "preparing":
            return datetime.now() + timedelta(minutes=30)
        elif delivery.status == "out_for_delivery":
            return datetime.now() + timedelta(minutes=delivery.estimated_duration)
        else:
            return datetime.now()

    def track_delivery(self, delivery: Delivery) -> dict:
        return {
            "delivery_id": delivery.delivery_id,
            "status": delivery.status,
            "assigned_person": delivery.delivery_person.name if delivery.delivery_person else "Not assigned",
            "eta": self.get_delivery_eta(delivery),
            "current_location": "In transit",  # This would come from GPS
            "distance_remaining": 2.5  # This would be calculated
        }

    @staticmethod
    def record_delivery_feedback(delivery: Delivery, rating: int):
        delivery.customer_rating = rating


    def get_delivery_performance(self) -> dict:
        on_time_deliveries = [d for d in self.completed_deliveries
                              if d.actual_delivery_time and
                              d.actual_delivery_time <= datetime.strptime(d.delivery_time,
                                                                          "%Y-%m-%d %H:%M") + timedelta(minutes=15)]

        on_time_rate = (len(on_time_deliveries) / len(
            self.completed_deliveries)) * 100 if self.completed_deliveries else 0

        return {
            "total_deliveries_today": len(self.completed_deliveries),
            "on_time_delivery_rate": on_time_rate,
            "average_rating": sum(d.customer_rating for d in self.completed_deliveries) / len(
                self.completed_deliveries) if self.completed_deliveries else 0,
            "active_deliveries": len(self.active_deliveries)
        }