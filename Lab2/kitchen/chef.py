from kitchen.recipe import Recipe


class Chef:
    def __init__(self, chef_id, name):
        self.chef_id = chef_id
        self.name = name
        self.specialty = ""
        self.recipes = []

    def create_recipe(self, recipe_name):
        new_recipe = Recipe(recipe_name, "")
        self.recipes.append(new_recipe)
        return f"Created recipe: {recipe_name}"

    def train_staff(self, staff_member):
        return f"Training {staff_member}"