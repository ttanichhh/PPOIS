from support.reservation import Reservation
from core.table import Table
from exceptions.restaurant_exceptions import ReservationException

class ReservationManagement:
    def __init__(self):
        self.reservations = []
        self.waiting_list = []

    def make_reservation(self, reservation: Reservation):
        if self.is_table_available(reservation.table):  # Убрал reservation_time
            self.reservations.append(reservation)
            reservation.table.is_reserved = True
            return True
        else:
            self.waiting_list.append(reservation)
            return False

    @staticmethod
    def is_table_available(table: Table) -> bool:  # Убрал reservation_time
        return not table.is_occupied and not table.is_reserved