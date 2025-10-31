from core.customer import Customer
from exceptions.restaurant_exceptions import CustomerException


class LoyaltyManager:
    def __init__(self):
        self.rewards_catalog = []

    def add_reward(self, name: str, points_required: int):
        self.rewards_catalog.append({
            "name": name,
            "points_required": points_required
        })

    def get_available_rewards(self, customer: Customer) -> list:
        return [reward for reward in self.rewards_catalog
                if reward["points_required"] <= customer.loyalty_points]

    def redeem_reward(self, customer: Customer, reward_name: str) -> bool:
        reward = next((r for r in self.rewards_catalog if r["name"] == reward_name), None)
        if not reward or reward["points_required"] > customer.loyalty_points:
            return False

        customer.use_loyalty_points(reward["points_required"])
        return True