from finance.ExpenseTracker import ExpenseTracker


class FinanceManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.budget = 0.0
        self.expense_tracker = ExpenseTracker()

    def analyze_financial_data(self):
        revenue = 25000.50
        expenses = 18000.75
        profit = revenue - expenses
        margin = (profit / revenue) * 100

        analysis = f"Financial Analysis - {self.name}\n"
        analysis += f"Revenue: ${revenue:.2f}\n"
        analysis += f"Expenses: ${expenses:.2f}\n"
        analysis += f"Profit: ${profit:.2f}\n"
        analysis += f"Margin: {margin:.1f}%"
        return analysis

    def create_budget_plan(self):
        departments = ["Kitchen", "Service", "Marketing", "Maintenance"]
        allocations = [40, 30, 20, 10]

        plan = f"Budget Plan - Total: ${self.budget:.2f}\n"
        for dept, alloc in zip(departments, allocations):
            amount = self.budget * (alloc / 100)
            plan += f"{dept}: ${amount:.2f} ({alloc}%)\n"
        return plan