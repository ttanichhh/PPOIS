class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []
        self.monthly_budget = 0.0

    def add_expense(self, amount, category):
        if amount <= 0:
            return "Expense amount must be positive"

        self.expenses.append((amount, category))
        if category not in self.categories:
            self.categories.append(category)

        monthly_expenses = sum(exp[0] for exp in self.expenses)
        budget_remaining = self.monthly_budget - monthly_expenses

        status = "🟢 Within budget" if budget_remaining >= 0 else "🔴 Over budget"

        return f"Expense recorded: ${amount:.2f} for {category}\nMonthly total: ${monthly_expenses:.2f}\nBudget status: {status}"

    def get_total_expenses(self):
        if not self.expenses:
            return "No expenses recorded"

        category_totals = {}
        for amount, category in self.expenses:
            category_totals[category] = category_totals.get(category, 0) + amount

        total = sum(category_totals.values())
        highest_category = max(category_totals.items(), key=lambda x: x[1]) if category_totals else ("None", 0)

        return f"Total Expenses: ${total:.2f}\nHighest category: {highest_category[0]} (${highest_category[1]:.2f})"