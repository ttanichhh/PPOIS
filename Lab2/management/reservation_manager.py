from entities.reservation import Reservation


class ReservationManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.reservations = []

    def check_availability(self, date, time):
        return f"Checking availability for {date} {time}"

    def confirm_reservation(self, reservation):
        return f"Reservation {reservation.reservation_id} confirmed"