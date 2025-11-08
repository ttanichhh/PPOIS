from kitchen.Ingredient import Ingredient


class Dish:
    def __init__(self, dish_id, name):
        self.dish_id = dish_id
        self.name = name
        self.ingredients = []
        self.preparation_time = 0

    def add_ingredient(self, ingredient):
        existing_ingredients = [i.name for i in self.ingredients]
        if ingredient.name in existing_ingredients:
            return f"Ingredient {ingredient.name} already in dish"

        self.ingredients.append(ingredient)
        self.preparation_time = self.calculate_prep_time()

        ingredient_list = ", ".join([i.name for i in self.ingredients])
        return f"Added {ingredient.name}. Ingredients: {ingredient_list}"

    def calculate_prep_time(self):
        base_time = 10
        ingredient_time = len(self.ingredients) * 2
        complexity_bonus = 0

        if any(i.name.lower() in ["sauce", "marinade"] for i in self.ingredients):
            complexity_bonus += 5
        if len(self.ingredients) > 5:
            complexity_bonus += 3

        total_time = base_time + ingredient_time + complexity_bonus
        self.preparation_time = total_time
        return total_time