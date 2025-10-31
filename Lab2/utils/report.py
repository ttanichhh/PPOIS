from datetime import datetime, timedelta
from core.restaurant import Restaurant

class Report:
    def __init__(self, report_id: int, report_type: str, content: dict, generated_at: datetime):
        self.report_id = report_id
        self.report_type = report_type
        self.content = content
        self.generated_at = generated_at
        self.period_start = None
        self.period_end = None
        self.format = "pdf"
        self.is_scheduled = False
        self.recipients = []


class ReportGenerator:
    def __init__(self, restaurant: Restaurant):
        self.restaurant = restaurant
        self.generated_reports = []
        self.report_templates = {}
        self.scheduled_reports = []
        self.export_formats = ["pdf", "excel", "csv"]

    def generate_sales_report(self, start_date: str, end_date: str) -> Report:
        # Simulate sales data analysis
        total_sales = 15000.0
        average_order_value = 45.0
        popular_items = ["Spaghetti Carbonara", "Margherita Pizza", "Caesar Salad"]

        content = {
            "report_type": "sales",
            "period": f"{start_date} to {end_date}",
            "total_sales": total_sales,
            "average_order_value": average_order_value,
            "popular_items": popular_items,
            "sales_by_category": {
                "appetizers": 3000.0,
                "main_courses": 9000.0,
                "desserts": 2000.0,
                "beverages": 1000.0
            }
        }

        report = Report(
            len(self.generated_reports) + 1,
            "sales_report",
            content,
            datetime.now()
        )
        self.generated_reports.append(report)
        return report

    def generate_inventory_report(self) -> Report:
        low_stock_items = []
        expired_items = []
        total_inventory_value = 5000.0

        content = {
            "report_type": "inventory",
            "total_inventory_value": total_inventory_value,
            "low_stock_items": low_stock_items,
            "expired_items": expired_items,
            "inventory_turnover": 4.2
        }

        report = Report(
            len(self.generated_reports) + 1,
            "inventory_report",
            content,
            datetime.now()
        )
        self.generated_reports.append(report)
        return report

    def generate_employee_performance_report(self) -> Report:
        top_performers = []
        attendance_records = {}
        training_completion = {}

        content = {
            "report_type": "employee_performance",
            "top_performers": top_performers,
            "attendance_summary": attendance_records,
            "training_status": training_completion,
            "average_rating": 4.5
        }

        report = Report(
            len(self.generated_reports) + 1,
            "employee_performance_report",
            content,
            datetime.now()
        )
        self.generated_reports.append(report)
        return report

    def generate_financial_report(self, period: str) -> Report:
        revenue = 20000.0
        expenses = 12000.0
        profit = revenue - expenses
        profit_margin = (profit / revenue) * 100

        content = {
            "report_type": "financial",
            "period": period,
            "revenue": revenue,
            "expenses": expenses,
            "profit": profit,
            "profit_margin": profit_margin,
            "expense_breakdown": {
                "food_costs": 6000.0,
                "labor_costs": 4000.0,
                "rent": 1500.0,
                "utilities": 500.0
            }
        }

        report = Report(
            len(self.generated_reports) + 1,
            "financial_report",
            content,
            datetime.now()
        )
        self.generated_reports.append(report)
        return report

    def schedule_daily_report(self, report_type: str, recipients: list):
        scheduled_report = {
            "report_type": report_type,
            "recipients": recipients,
            "schedule": "daily",
            "last_generated": None
        }
        self.scheduled_reports.append(scheduled_report)

    def get_report_by_id(self, report_id: int) -> Report:
        for report in self.generated_reports:
            if report.report_id == report_id:
                return report
        return None