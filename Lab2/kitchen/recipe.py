from kitchen.ingredient import Ingredient


class Recipe:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        self.ingredients = []
        self.cooking_time = 0

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredient_list(self):
        return [ingredient.name for ingredient in self.ingredients]