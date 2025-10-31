from exceptions.restaurant_exceptions import RestaurantException

class Expense:
    def __init__(self, expense_id: int, category: str, amount: float, date: str, description: str):
        self.expense_id = expense_id
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description
        self.payment_method = ""
        self.vendor = ""
        self.receipt_number = ""
        self.is_recurring = False
        self.approved_by = ""


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget_categories = {}
        self.expense_categories = ["food", "labor", "rent", "utilities", "supplies", "marketing", "maintenance"]
        self.monthly_budgets = {}
        self.approval_workflow = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        self.check_budget_alert(expense)

    def get_expenses_by_category(self, category: str, month: str) -> list:
        return [exp for exp in self.expenses if exp.category == category and exp.date.startswith(month)]

    def set_budget(self, category: str, monthly_amount: float):
        self.budget_categories[category] = monthly_amount

    def check_budget_alert(self, expense: Expense):
        if expense.category in self.budget_categories:
            monthly_budget = self.budget_categories[expense.category]
            monthly_expenses = sum(
                exp.amount for exp in self.get_expenses_by_category(expense.category, expense.date[:7]))

            if monthly_expenses > monthly_budget * 0.8:  # 80% threshold
                print(
                    f"Budget alert: {expense.category} spending at {monthly_expenses / monthly_budget * 100:.1f}% of budget")

    def generate_expense_report(self, start_date: str, end_date: str) -> dict:
        period_expenses = [exp for exp in self.expenses if start_date <= exp.date <= end_date]
        total_amount = sum(exp.amount for exp in period_expenses)

        category_breakdown = {}
        for category in self.expense_categories:
            category_expenses = [exp for exp in period_expenses if exp.category == category]
            category_breakdown[category] = sum(exp.amount for exp in category_expenses)

        return {
            "period": f"{start_date} to {end_date}",
            "total_expenses": total_amount,
            "category_breakdown": category_breakdown,
            "largest_expense": max(period_expenses, key=lambda x: x.amount).amount if period_expenses else 0
        }