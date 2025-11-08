class BudgetPlanner:
    def __init__(self):
        self.budget_categories = []
        self.allocated_amounts = {}

    def allocate_budget(self, category, amount):
        if amount < 0:
            return "Budget amount cannot be negative"

        self.allocated_amounts[category] = amount
        if category not in self.budget_categories:
            self.budget_categories.append(category)

        total_budget = sum(self.allocated_amounts.values())
        category_percent = (amount / total_budget) * 100 if total_budget > 0 else 0

        return f"Allocated ${amount:.2f} to {category}\nRepresents {category_percent:.1f}% of total budget"

    def check_budget_usage(self):
        if not self.allocated_amounts:
            return "No budgets allocated"

        total_allocated = sum(self.allocated_amounts.values())
        usage_report = f"Budget Allocation Summary\n"
        usage_report += f"Total Budget: ${total_allocated:.2f}\n"
        usage_report += "Category Breakdown:\n"

        for category, amount in self.allocated_amounts.items():
            percentage = (amount / total_allocated) * 100
            usage_report += f"• {category}: ${amount:.2f} ({percentage:.1f}%)\n"

        return usage_report