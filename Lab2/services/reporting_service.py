from datetime import datetime, timedelta
from utils.report import ReportGenerator


class ReportingService:
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self.report_generator = ReportGenerator(restaurant)
        self.scheduled_reports = []
        self.report_subscribers = []
        self.data_sources = []
        self.analytics_cache = {}

    def generate_daily_operations_report(self) -> dict:
        today = datetime.now().strftime("%Y-%m-%d")

        # Collect various metrics
        total_orders = len([order for order in self.restaurant.orders
                            if str(order.order_time).startswith(today)])
        total_revenue = sum(order.total_amount for order in self.restaurant.orders
                            if str(order.order_time).startswith(today))
        occupied_tables = len([table for table in self.restaurant.tables if table.is_occupied])

        report_data = {
            "date": today,
            "total_orders": total_orders,
            "total_revenue": total_revenue,
            "average_order_value": total_revenue / total_orders if total_orders > 0 else 0,
            "table_occupancy_rate": (occupied_tables / len(self.restaurant.tables)) * 100,
            "peak_hours": self._calculate_peak_hours(today),
            "popular_items": self._get_todays_popular_items(today)
        }

        return report_data

    def generate_weekly_financial_report(self) -> dict:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)

        weekly_orders = [order for order in self.restaurant.orders
                         if start_date <= order.order_time <= end_date]

        total_revenue = sum(order.total_amount for order in weekly_orders)
        total_customers = len(set(order.customer.customer_id for order in weekly_orders))

        return {
            "period": f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}",
            "total_revenue": total_revenue,
            "average_daily_revenue": total_revenue / 7,
            "unique_customers": total_customers,
            "customer_retention_rate": self._calculate_retention_rate(),
            "revenue_growth": self._calculate_revenue_growth()
        }

    @staticmethod
    def generate_employee_performance_report(period: str) -> dict:
        # This would aggregate data from various sources
        performance_data = {
            "period": period,
            "top_performers": [],
            "training_completion": {},
            "attendance_rate": 95.5,
            "average_rating": 4.3,
            "sales_per_employee": {}
        }

        return performance_data

    def generate_customer_analytics_report(self) -> dict:
        total_customers = len(self.restaurant.customers)
        vip_customers = len([c for c in self.restaurant.customers if c.is_vip])
        new_customers_this_month = len([c for c in self.restaurant.customers
                                        if c.created_at and
                                        c.created_at.month == datetime.now().month])

        return {
            "total_customers": total_customers,
            "vip_customers": vip_customers,
            "new_customers_this_month": new_customers_this_month,
            "average_customer_value": self._calculate_average_customer_value(),
            "customer_satisfaction_score": 4.5,
            "repeat_customer_rate": 65.2
        }

    def _calculate_peak_hours(self, date: str) -> list:
        # Simplified peak hours calculation
        hour_counts = {hour: 0 for hour in range(9, 23)}

        for order in self.restaurant.orders:
            if str(order.order_time).startswith(date):
                hour = order.order_time.hour
                if hour in hour_counts:
                    hour_counts[hour] += 1

        # Return top 3 busiest hours
        return sorted(hour_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    def _get_todays_popular_items(self, date: str) -> list:
        item_counts = {}
        for order in self.restaurant.orders:
            if str(order.order_time).startswith(date):
                for item in order.order_items:
                    item_name = item.menu_item.name
                    item_counts[item_name] = item_counts.get(item_name, 0) + item.quantity

        return sorted(item_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    @staticmethod
    def _calculate_retention_rate() -> float:  # Убрал неиспользуемые параметры
        # Simplified retention rate calculation
        return 75.5  # This would be calculated based on customer visit patterns

    @staticmethod
    def _calculate_revenue_growth() -> float:  # Убрал неиспользуемые параметры
        # Simplified revenue growth calculation
        return 12.3  # This would compare with previous period

    def _calculate_average_customer_value(self) -> float:
        if not self.restaurant.customers:
            return 0.0
        total_spent = sum(customer.total_spent for customer in self.restaurant.customers)
        return total_spent / len(self.restaurant.customers)

    def schedule_automatic_report(self, report_type: str, frequency: str, recipients: list):
        scheduled_report = {
            "report_type": report_type,
            "frequency": frequency,
            "recipients": recipients,
            "last_sent": None,
            "is_active": True
        }
        self.scheduled_reports.append(scheduled_report)

    def send_report_to_subscribers(self):
        for subscriber in self.report_subscribers:
            # In a real system, this would send emails or notifications
            print(f"Sending report to {subscriber['email']}")