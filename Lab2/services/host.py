from entities.reservation import Reservation


class Host:
    def __init__(self, host_id, name):
        self.host_id = host_id
        self.name = name
        self.greeting = ""

    def greet_customer(self, customer):
        return f"Welcome {customer.name}!"

    def seat_customer(self, table):
        return f"Seated at table {table.table_id}"