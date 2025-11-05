class BudgetPlanner:
    def __init__(self):
        self.budget_categories = []
        self.allocated_amounts = {}

    def allocate_budget(self, category, amount):
        self.allocated_amounts[category] = amount

    def check_budget_usage(self):
        return "Budget usage checked"