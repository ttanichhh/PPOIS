
class Revenue:
    def __init__(self, revenue_id: int, source: str, amount: float, date: str):
        self.revenue_id = revenue_id
        self.source = source
        self.amount = amount
        self.date = date
        self.payment_method = ""
        self.order_id = ""
        self.tax_amount = 0.0
        self.discount_amount = 0.0


class RevenueManager:
    def __init__(self):
        self.revenue_streams = []
        self.daily_revenue = {}
        self.revenue_goals = {}
        self.growth_metrics = {}
        self.seasonal_patterns = {}

    def record_revenue(self, revenue: Revenue):
        self.revenue_streams.append(revenue)
        self.update_daily_revenue(revenue.date, revenue.amount)

    def update_daily_revenue(self, date: str, amount: float):
        if date not in self.daily_revenue:
            self.daily_revenue[date] = 0.0
        self.daily_revenue[date] += amount

    def get_revenue_by_period(self, start_date: str, end_date: str) -> float:
        total = 0.0
        current_date = start_date
        while current_date <= end_date:
            total += self.daily_revenue.get(current_date, 0.0)
            # Increment date (simplified)
            current_date = "2024-01-21"  # This would be calculated properly
        return total

    def calculate_growth_rate(self, current_period: str, previous_period: str) -> float:
        current_revenue = self.get_revenue_by_period(current_period, current_period)
        previous_revenue = self.get_revenue_by_period(previous_period, previous_period)

        if previous_revenue == 0:
            return 0.0
        return ((current_revenue - previous_revenue) / previous_revenue) * 100

    def set_revenue_goal(self, period: str, target_amount: float):
        self.revenue_goals[period] = target_amount

    def check_goal_achievement(self, period: str) -> dict:
        actual_revenue = self.get_revenue_by_period(period, period)
        target_revenue = self.revenue_goals.get(period, 0)

        achievement_percentage = (actual_revenue / target_revenue * 100) if target_revenue > 0 else 0

        return {
            "period": period,
            "target": target_revenue,
            "actual": actual_revenue,
            "achievement_percentage": achievement_percentage,
            "on_track": achievement_percentage >= 100
        }