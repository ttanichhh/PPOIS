from kitchen.Dish import Dish


class FoodPreparation:
    def __init__(self, prep_id):
        self.prep_id = prep_id
        self.prep_steps = []
        self.quality_checks = []

    def add_prep_step(self, step):
        if step in self.prep_steps:
            return f"Step '{step}' already exists"

        self.prep_steps.append(step)

        step_categories = {
            "chop": "Preparation",
            "slice": "Preparation",
            "marinate": "Flavor",
            "cook": "Cooking",
            "plate": "Presentation"
        }

        category = "General"
        for key, cat in step_categories.items():
            if key in step.lower():
                category = cat
                break

        return f"Added step: '{step}' (Category: {category}). Total steps: {len(self.prep_steps)}"

    def perform_quality_check(self):
        checks = [
            "Ingredient freshness verified",
            "Cooking temperature optimal",
            "Presentation standards met",
            "Portion size correct",
            "Garnish properly applied"
        ]

        self.quality_checks.extend(checks)

        quality_report = f"Quality Check #{len(self.quality_checks) // 5}\n"
        for check in checks:
            quality_report += f"✓ {check}\n"
        quality_report += "Result: All quality standards met"
        return quality_report