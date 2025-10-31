from core.customer import Customer
from exceptions.restaurant_exceptions import CustomerException


class Reward:
    def __init__(self, reward_id: int, name: str, points_required: int, description: str):
        self.reward_id = reward_id
        self.name = name
        self.points_required = points_required
        self.description = description
        self.category = ""
        self.is_active = True
        self.stock_quantity = 0
        self.expiry_date = None
        self.min_tier_required = "Basic"


class LoyaltyManager:
    def __init__(self):
        self.rewards_catalog = []
        self.redemption_history = []
        self.tier_requirements = {
            "Basic": 0,
            "Silver": 500,
            "Gold": 1000,
            "Platinum": 2000
        }
        self.tier_benefits = {
            "Basic": {"points_multiplier": 1.0, "discount": 0.0},
            "Silver": {"points_multiplier": 1.2, "discount": 0.05},
            "Gold": {"points_multiplier": 1.5, "discount": 0.1},
            "Platinum": {"points_multiplier": 2.0, "discount": 0.15}
        }
        self.promotional_offers = []

    def add_reward(self, reward: Reward):
        self.rewards_catalog.append(reward)

    def get_available_rewards(self, customer: Customer) -> list:
        return [reward for reward in self.rewards_catalog
                if reward.is_active and
                reward.points_required <= customer.loyalty_points and
                self._check_tier_requirement(customer, reward)]

    def _check_tier_requirement(self, customer: Customer, reward: Reward) -> bool:
        customer_tier_level = list(self.tier_requirements.keys()).index(customer.membership_tier)
        required_tier_level = list(self.tier_requirements.keys()).index(reward.min_tier_required)
        return customer_tier_level >= required_tier_level

    def redeem_reward(self, customer: Customer, reward: Reward) -> bool:
        if reward not in self.get_available_rewards(customer):
            raise CustomerException("Reward not available for redemption")

        if reward.stock_quantity <= 0:
            raise CustomerException("Reward out of stock")

        customer.use_loyalty_points(reward.points_required)
        reward.stock_quantity -= 1

        redemption_record = {
            "customer_id": customer.customer_id,
            "reward_id": reward.reward_id,
            "points_used": reward.points_required,
            "redemption_date": "2024-01-20",
            "status": "completed"
        }
        self.redemption_history.append(redemption_record)

        return True

    def update_customer_tier(self, customer: Customer):
        current_points = customer.loyalty_points
        new_tier = "Basic"

        for tier, requirement in sorted(self.tier_requirements.items(),
                                        key=lambda x: x[1], reverse=True):
            if current_points >= requirement:
                new_tier = tier
                break

        if new_tier != customer.membership_tier:
            customer.membership_tier = new_tier
            return True
        return False

    def calculate_points_earned(self, customer: Customer, purchase_amount: float) -> int:
        multiplier = self.tier_benefits[customer.membership_tier]["points_multiplier"]
        base_points = int(purchase_amount)  # 1 point per dollar
        return int(base_points * multiplier)

    def get_tier_benefits(self, tier: str) -> dict:
        return self.tier_benefits.get(tier, {"points_multiplier": 1.0, "discount": 0.0})

    def add_promotional_offer(self, name: str, bonus_points: int, valid_until: str):
        offer = {
            "name": name,
            "bonus_points": bonus_points,
            "valid_until": valid_until,
            "is_active": True
        }
        self.promotional_offers.append(offer)