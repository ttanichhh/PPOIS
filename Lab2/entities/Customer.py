class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = ""
        self.loyalty_points = 0

    def add_loyalty_points(self, points):
        if points <= 0:
            return "Error: Points must be positive"

        old_tier = self._get_tier()
        self.loyalty_points += points
        new_tier = self._get_tier()

        if new_tier != old_tier:
            return f"Upgraded to {new_tier}! Total: {self.loyalty_points}"
        return f"Added {points} points. Total: {self.loyalty_points}"

    def get_customer_info(self):
        tier = self._get_tier()
        info = f"Customer: {self.name}\n"
        info += f"ID: {self.customer_id}\n"
        info += f"Phone: {self.phone}\n"
        info += f"Tier: {tier}\n"
        info += f"Points: {self.loyalty_points}"
        return info

    def _get_tier(self):
        if self.loyalty_points >= 1000:
            return "GOLD"
        elif self.loyalty_points >= 500:
            return "SILVER"
        return "BRONZE"