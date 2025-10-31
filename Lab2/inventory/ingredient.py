class Ingredient:
    def __init__(self, ingredient_id: int, name: str, unit: str, category: str):
        self.ingredient_id = ingredient_id
        self.name = name
        self.unit = unit
        self.category = category
        self.allergens = []
        self.nutritional_info = {}
        self.shelf_life_days = 0
        self.storage_temperature = ""
        self.is_organic = False
        self.is_gluten_free = False

    def add_allergen(self, allergen: str):
        self.allergens.append(allergen)

    def set_nutritional_info(self, calories: int, protein: float, carbs: float, fat: float):
        self.nutritional_info = {
            "calories": calories,
            "protein": protein,
            "carbs": carbs,
            "fat": fat
        }