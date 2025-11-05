from kitchen.ingredient import Ingredient


class Dish:
    def __init__(self, dish_id, name):
        self.dish_id = dish_id
        self.name = name
        self.ingredients = []
        self.preparation_time = 0

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def calculate_prep_time(self):
        return len(self.ingredients) * 2 + 10