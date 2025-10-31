from inventory.ingredient import Ingredient

class Recipe:
    def __init__(self, recipe_id: int, name: str, instructions: str):
        self.recipe_id = recipe_id
        self.name = name
        self.instructions = instructions
        self.ingredients = []

    def add_ingredient(self, ingredient: Ingredient, quantity: float):
        self.ingredients.append((ingredient, quantity))