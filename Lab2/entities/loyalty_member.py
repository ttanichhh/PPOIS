from entities.customer import Customer


class LoyaltyMember:
    def __init__(self, customer):
        self.customer = customer
        self.member_since = ""
        self.tier = "bronze"
        self.points_balance = 0

    def upgrade_tier(self):
        if self.points_balance >= 1000:
            self.tier = "gold"
        elif self.points_balance >= 500:
            self.tier = "silver"

    def get_member_info(self):
        return f"{self.customer.name} - {self.tier} tier"