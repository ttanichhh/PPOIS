from core.restaurant import Restaurant

class ReportGenerator:
    def __init__(self, restaurant: Restaurant):
        self.restaurant = restaurant
        self.generated_reports = []

    def generate_sales_report(self, start_date: str, end_date: str) -> dict:
        total_orders = len([order for order in self.restaurant.orders
                            if start_date <= str(order.order_time) <= end_date])
        total_revenue = sum(order.total_amount for order in self.restaurant.orders
                            if start_date <= str(order.order_time) <= end_date)

        return {
            "period": f"{start_date} to {end_date}",
            "total_orders": total_orders,
            "total_revenue": total_revenue
        }