from core.customer import Customer
from exceptions.restaurant_exceptions import CustomerException

class CustomerManagement:
    def __init__(self):
        self.customers = []
        self.loyalty_program = LoyaltyProgram()

    def register_customer(self, customer: Customer):
        if any(cust.customer_id == customer.customer_id for cust in self.customers):
            raise CustomerException("Customer ID already exists")
        self.customers.append(customer)
        self.loyalty_program.enroll_customer(customer)

    def find_customer_by_id(self, customer_id: int) -> Customer:
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

class LoyaltyProgram:
    def __init__(self):
        self.points_earn_rate = 10

    @staticmethod
    def enroll_customer(customer: Customer):
        customer.loyalty_points = 0