from entities.Customer import Customer

class LoyaltyMember:
    def __init__(self, customer):
        self.customer = customer
        self.member_since = ""
        self.tier = "bronze"
        self.points_balance = 0

    def upgrade_tier(self):
        old_tier = self.tier
        if self.points_balance >= 1000:
            self.tier = "gold"
        elif self.points_balance >= 500:
            self.tier = "silver"
        else:
            self.tier = "bronze"

        if old_tier != self.tier:
            return f"Upgraded from {old_tier} to {self.tier} tier"
        return f"Remains in {self.tier} tier"

    def get_member_info(self):
        info = f"Loyalty Member: {self.customer.name}\n"
        info += f"Tier: {self.tier.upper()}\n"
        info += f"Points: {self.points_balance}\n"
        info += f"Member since: {self.member_since if self.member_since else 'Not specified'}"
        return info