from finance.expense_tracker import ExpenseTracker


class FinanceManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.budget = 0.0
        self.expense_tracker = ExpenseTracker()

    def analyze_financial_data(self):
        return "Financial data analyzed"

    def create_budget_plan(self):
        return "Budget plan created"