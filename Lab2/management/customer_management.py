from core.customer import Customer
from exceptions.restaurant_exceptions import CustomerException

class CustomerManagement:
    def __init__(self):
        self.customers = []
        self.loyalty_program = LoyaltyProgram()
        self.feedback_records = []
        self.marketing_campaigns = []
        self.customer_segments = {}
        self.retention_metrics = {}

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

    def find_customer_by_email(self, email: str) -> Customer:
        for customer in self.customers:
            if customer.email.lower() == email.lower():
                return customer
        return None

    @staticmethod
    def update_customer_tier(customer: Customer):
        if customer.total_spent > 1000:
            customer.membership_tier = "Gold"
        elif customer.total_spent > 500:
            customer.membership_tier = "Silver"

    def get_top_customers(self, limit: int = 10) -> list:
        return sorted(self.customers, key=lambda x: x.total_spent, reverse=True)[:limit]

    def record_feedback(self, customer: Customer, rating: int, comments: str):
        self.feedback_records.append({
            "customer_id": customer.customer_id,
            "rating": rating,
            "comments": comments,
            "date": "2024-01-20"
        })

    @staticmethod
    def send_promotion(customer: Customer, promotion: str):
        # In a real system, this would send an email or notification
        print(f"Sent promotion to {customer.email}: {promotion}")

class LoyaltyProgram:
    def __init__(self):
        self.points_earn_rate = 10  # points per $ spent
        self.rewards_catalog = []
        self.redemption_history = []

    @staticmethod
    def enroll_customer(customer: Customer):
        customer.loyalty_points = 0
        customer.membership_tier = "Basic"

    def earn_points(self, customer: Customer, purchase_amount: float):
        points_earned = int(purchase_amount * self.points_earn_rate)
        customer.add_loyalty_points(points_earned)

    def redeem_points(self, customer: Customer, reward):
        if customer.loyalty_points >= reward.points_required:
            customer.use_loyalty_points(reward.points_required)
            self.redemption_history.append({
                "customer_id": customer.customer_id,
                "reward": reward.name,
                "points_used": reward.points_required,
                "date": "2024-01-20"
            })
            return True
        return False