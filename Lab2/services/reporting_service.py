from datetime import datetime

class ReportingService:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def generate_daily_operations_report(self) -> dict:
        today = datetime.now().strftime("%Y-%m-%d")
        total_orders = len([order for order in self.restaurant.orders
                            if str(order.order_time).startswith(today)])
        total_revenue = sum(order.total_amount for order in self.restaurant.orders
                            if str(order.order_time).startswith(today))

        return {
            "date": today,
            "total_orders": total_orders,
            "total_revenue": total_revenue
        }