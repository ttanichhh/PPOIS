from support.person import Person
from exceptions.restaurant_exceptions import CustomerException

class Customer(Person):
    def __init__(self, customer_id: int, name: str, phone: str, email: str,
                 loyalty_points: int = 0):
        super().__init__(customer_id, name, phone, email)
        self.customer_id = customer_id
        self.loyalty_points = loyalty_points
        self.order_history = []


    def add_loyalty_points(self, points: int):
        if points <= 0:
            raise CustomerException("Points must be positive")
        self.loyalty_points += points

    def use_loyalty_points(self, points: int):
        if points > self.loyalty_points:
            raise CustomerException("Not enough loyalty points")
        self.loyalty_points -= points

    def record_visit(self, amount_spent: float):
        self.visits_count += 1
        self.total_spent += amount_spent
