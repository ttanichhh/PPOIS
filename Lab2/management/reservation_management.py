from support.reservation import Reservation
from core.table import Table
from exceptions.restaurant_exceptions import ReservationException
from datetime import datetime


class ReservationManagement:
    def __init__(self):
        self.reservations = []
        self.waiting_list = []
        self.table_assignments = {}
        self.reservation_slots = {}
        self.cancellation_policy = {"hours": 2, "fee_percentage": 50}
        self.no_show_records = []

    def make_reservation(self, reservation: Reservation):
        if self.is_table_available(reservation.table, reservation.reservation_time):
            self.reservations.append(reservation)
            reservation.table.is_reserved = True
            reservation.table.current_reservation = reservation
            return True
        else:
            self.waiting_list.append(reservation)
            return False

    def cancel_reservation(self, reservation_id: int, reason: str = ""):
        reservation = self.find_reservation_by_id(reservation_id)
        if reservation:
            reservation.cancel_reservation(reason)
            self.reservations.remove(reservation)

            # Check if we can accommodate waiting list
            self.process_waiting_list()
            return True
        return False

    def find_reservation_by_id(self, reservation_id: int) -> Reservation:
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                return reservation
        return None

    def is_table_available(self, table: Table, reservation_time: str) -> bool:
        # Check if table is not occupied and not reserved at the given time
        if table.is_occupied or table.is_reserved:
            return False

        # Check for overlapping reservations
        for existing_reservation in self.reservations:
            if existing_reservation.table.table_id == table.table_id:
                existing_time = datetime.strptime(existing_reservation.reservation_time, "%Y-%m-%d %H:%M")
                new_time = datetime.strptime(reservation_time, "%Y-%m-%d %H:%M")
                time_diff = abs((new_time - existing_time).total_seconds() / 3600)

                if time_diff < 2:  # 2 hours gap between reservations
                    return False
        return True

    def process_waiting_list(self):
        for reservation in self.waiting_list[:]:
            if self.is_table_available(reservation.table, reservation.reservation_time):
                self.make_reservation(reservation)
                self.waiting_list.remove(reservation)

    def get_reservations_for_date(self, date: str) -> list:
        return [res for res in self.reservations if res.reservation_time.startswith(date)]

    def record_no_show(self, reservation: Reservation):
        self.no_show_records.append({
            "reservation_id": reservation.reservation_id,
            "customer_id": reservation.customer.customer_id,
            "date": reservation.reservation_time,
            "penalty_applied": True
        })