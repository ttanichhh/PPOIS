from exceptions.restaurant_exceptions import ReservationException  # 🔹 ИСПРАВЛЕНО
from datetime import datetime

class Reservation:
    def __init__(self, reservation_id: int, customer, table,
                 reservation_time: str, guests_count: int, duration: int = 120):
        self.reservation_id = reservation_id
        self.customer = customer
        self.table = table
        self.reservation_time = reservation_time
        self.guests_count = guests_count
        self.duration = duration
        self.status = "confirmed"
        self.created_at = datetime.now()
        self.special_requests = ""
        self.occasion = ""
        self.arrival_time = None
        self.departure_time = None
        self.deposit_amount = 0.0
        self.cancellation_reason = ""

    def cancel_reservation(self, reason: str = ""):
        self.status = "cancelled"
        self.table.free_table()
        self.cancellation_reason = reason

    def mark_arrival(self):
        self.arrival_time = datetime.now()
        self.status = "arrived"

    def mark_departure(self):
        self.departure_time = datetime.now()
        self.status = "completed"

    def update_guest_count(self, new_count: int):
        if new_count > self.table.capacity:
            raise ReservationException("Guest count exceeds table capacity")
        self.guests_count = new_count