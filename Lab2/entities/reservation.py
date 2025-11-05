from entities.customer import Customer


class Reservation:
    def __init__(self, reservation_id, customer, date):
        self.reservation_id = reservation_id
        self.customer = customer
        self.date = date
        self.guests = 2
        self.table_number = 0

    def update_guests(self, new_guests):
        self.guests = new_guests

    def get_reservation_info(self):
        return f"Reservation for {self.customer.name} on {self.date}"