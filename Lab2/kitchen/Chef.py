from kitchen.Recipe import Recipe


class Chef:
    def __init__(self, chef_id, name):
        self.chef_id = chef_id
        self.name = name
        self.specialty = ""
        self.recipes = []

    def create_recipe(self, recipe_name):
        existing_names = [r.name for r in self.recipes]
        if recipe_name in existing_names:
            return f"Recipe '{recipe_name}' already exists"

        new_recipe = Recipe(recipe_name, "Add instructions here")
        self.recipes.append(new_recipe)

        specialties = {}
        for recipe in self.recipes:
            if "pasta" in recipe.name.lower():
                specialties["pasta"] = specialties.get("pasta", 0) + 1
            elif "sauce" in recipe.name.lower():
                specialties["sauce"] = specialties.get("sauce", 0) + 1

        return f"Created '{recipe_name}'. Total recipes: {len(self.recipes)}"

    def train_kitchen_staff(self):
        training_modules = [
            "Food safety and hygiene",
            "Knife skills and techniques",
            "Recipe preparation standards",
            "Plating and presentation",
            "Kitchen equipment usage"
        ]

        training_plan = f"Kitchen Training by Chef {self.name}\n"
        for i, module in enumerate(training_modules, 1):
            training_plan += f"{i}. {module}\n"
        training_plan += "Duration: 2 weeks"
        return training_plan