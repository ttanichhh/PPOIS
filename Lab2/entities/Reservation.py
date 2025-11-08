from entities.Customer import Customer

class Reservation:
    def __init__(self, reservation_id, customer, date):
        self.reservation_id = reservation_id
        self.customer = customer
        self.date = date
        self.guests = 2
        self.table_number = 0

    def update_guests(self, new_guests):
        if new_guests < 1:
            return "Must have at least 1 guest"
        if new_guests > 10:
            return "Maximum 10 guests per reservation"

        old_guests = self.guests
        self.guests = new_guests
        return f"Updated from {old_guests} to {new_guests} guests"

    def get_reservation_info(self):
        info = f"Reservation #{self.reservation_id}\n"
        info += f"Customer: {self.customer.name}\n"
        info += f"Date: {self.date}\n"
        info += f"Guests: {self.guests}\n"
        info += f"Table: {self.table_number if self.table_number else 'Not assigned'}"
        return info