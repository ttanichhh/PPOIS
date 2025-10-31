from inventory.ingredient import Ingredient

class Recipe:
    def __init__(self, recipe_id: int, name: str, instructions: str, preparation_time: int):
        self.recipe_id = recipe_id
        self.name = name
        self.instructions = instructions
        self.preparation_time = preparation_time
        self.ingredients = []  # List of tuples (Ingredient, quantity)
        self.difficulty_level = "medium"
        self.servings = 1
        self.cuisine_type = ""
        self.is_secret = False
        self.creation_date = "2024-01-20"

    def add_ingredient(self, ingredient: Ingredient, quantity: float):
        self.ingredients.append((ingredient, quantity))

    def get_total_cost(self) -> float:
        total = 0.0
        for ingredient, quantity in self.ingredients:
            # This would use ingredient cost from inventory
            total += quantity * 2.5  # Placeholder cost
        return total