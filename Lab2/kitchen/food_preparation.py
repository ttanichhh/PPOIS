from kitchen.dish import Dish


class FoodPreparation:
    def __init__(self, prep_id):
        self.prep_id = prep_id
        self.prep_steps = []
        self.quality_checks = []

    def add_prep_step(self, step):
        self.prep_steps.append(step)

    def perform_quality_check(self):
        return "Quality check performed"