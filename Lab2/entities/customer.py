class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = ""
        self.loyalty_points = 0

    def add_loyalty_points(self, points):
        self.loyalty_points += points
        return f"Added {points} points. Total: {self.loyalty_points}"

    def get_customer_info(self):
        return f"{self.name} ({self.phone})"