from entities.Reservation import Reservation


class Host:
    def __init__(self, host_id, name):
        self.host_id = host_id
        self.name = name
        self.greeting = ""

    def greet_customer(self, customer):
        greetings = [
            f"Welcome to our restaurant, {customer.name}!",
            f"Good evening, {customer.name}. We're delighted to have you!",
            f"Hello {customer.name}, your table is being prepared.",
            f"Welcome back, {customer.name}! So nice to see you again."
        ]

        import random
        greeting = random.choice(greetings)

        if customer.loyalty_points > 500:
            greeting += " Thank you for being a loyal customer!"

        return f" {self.name}: \"{greeting}\""

    def seat_customer(self, table):
        if table.is_occupied:
            return f"Cannot seat at table {table.table_id} - already occupied"

        table.occupy_table()

        seating_info = f"Seated at table {table.table_id}\n"
        seating_info += f"Location: {table.location}\n"
        seating_info += f"Capacity: {table.capacity} guests\n"
        seating_info += f"Host: {self.name}"
        return seating_info