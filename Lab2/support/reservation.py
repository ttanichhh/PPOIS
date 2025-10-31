from exceptions.restaurant_exceptions import ReservationException

class Reservation:
    def __init__(self, reservation_id: int, customer, table, reservation_time: str, guests_count: int):
        self.reservation_id = reservation_id
        self.customer = customer
        self.table = table
        self.reservation_time = reservation_time
        self.guests_count = guests_count
        self.status = "confirmed"

    def cancel_reservation(self):
        self.status = "cancelled"
        self.table.free_table()