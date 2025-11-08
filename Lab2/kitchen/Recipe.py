from kitchen.Ingredient import Ingredient


class Recipe:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty_level = ""

    def add_ingredient(self, ingredient):
        if any(i.name == ingredient.name for i in self.ingredients):
            return f"{ingredient.name} already in recipe"

        self.ingredients.append(ingredient)

        # Auto-set difficulty based on ingredients
        if len(self.ingredients) <= 3:
            self.difficulty_level = "Easy"
        elif len(self.ingredients) <= 6:
            self.difficulty_level = "Medium"
        else:
            self.difficulty_level = "Hard"

        return f"Added {ingredient.name}. Difficulty: {self.difficulty_level}"

    def get_ingredient_list(self):
        if not self.ingredients:
            return "No ingredients added to recipe"

        ingredient_list = f"Ingredients for {self.name}:\n"
        for i, ingredient in enumerate(self.ingredients, 1):
            quantity_info = f"{ingredient.quantity}{ingredient.unit}" if ingredient.unit else str(ingredient.quantity)
            ingredient_list += f"{i}. {ingredient.name} - {quantity_info}\n"
        return ingredient_list