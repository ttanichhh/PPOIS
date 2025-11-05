class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []
        self.monthly_budget = 0.0

    def add_expense(self, amount, category):
        self.expenses.append((amount, category))

    def get_total_expenses(self):
        return sum(expense[0] for expense in self.expenses)