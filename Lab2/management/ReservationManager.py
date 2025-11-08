from entities.Reservation import Reservation


class ReservationManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.reservations = []

    def check_availability(self, date, time):
        time_slots = ["17:00", "18:00", "19:00", "20:00", "21:00"]
        available_tables = [1, 2, 3, 4, 5, 6, 7, 8]

        reservations_at_time = [
            r for r in self.reservations
            if r.date == date and abs(int(r.time.split(':')[0]) - int(time.split(':')[0])) < 2
        ]

        tables_taken = len(reservations_at_time)
        tables_available = len(available_tables) - tables_taken

        availability = f"Availability for {date} at {time}\n"
        availability += f"Tables available: {tables_available}\n"
        availability += f"Reservations: {len(reservations_at_time)}"
        return availability

    def confirm_reservation(self, reservation):
        conflicting_reservations = [
            r for r in self.reservations
            if r.date == reservation.date and r.table_number == reservation.table_number
        ]

        if conflicting_reservations:
            return f"Cannot confirm - table {reservation.table_number} already booked"

        self.reservations.append(reservation)
        return f"Reservation #{reservation.reservation_id} confirmed for {reservation.date}"