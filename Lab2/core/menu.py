from exceptions.restaurant_exceptions import MenuException

class MenuItem:
    def __init__(self, item_id: int, name: str, description: str, price: float,
                 category: str, preparation_time: int, calories: int = 0):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.preparation_time = preparation_time
        self.calories = calories
        self.ingredients = []
        self.is_available = True
        self.spice_level = 0
        self.is_vegetarian = False
        self.is_vegan = False
        self.is_gluten_free = False
        self.allergens = []
        self.popularity_score = 0
        self.cost_price = 0.0

    def update_price(self, new_price: float):
        if new_price < 0:
            raise MenuException("Price cannot be negative")
        self.price = new_price

    def add_allergen(self, allergen: str):
        self.allergens.append(allergen)

    def increment_popularity(self):
        self.popularity_score += 1

class MenuCategory:
    def __init__(self, category_id: int, name: str, description: str, display_order: int):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.display_order = display_order
        self.menu_items = []
        self.is_active = True
        self.image_url = ""
        self.available_times = ["all_day"]

    def add_menu_item(self, menu_item: MenuItem):
        self.menu_items.append(menu_item)

    def remove_menu_item(self, menu_item: MenuItem):
        self.menu_items.remove(menu_item)

class Menu:
    def __init__(self, menu_id: int, name: str, description: str):
        self.menu_id = menu_id
        self.name = name
        self.description = description
        self.categories = []
        self.last_updated = None
        self.is_active = True
        self.seasonal = False
        self.valid_from = None
        self.valid_to = None

    def add_category(self, category: MenuCategory):
        self.categories.append(category)

    def find_item_by_name(self, name: str):
        for category in self.categories:
            for item in category.menu_items:
                if item.name.lower() == name.lower():
                    return item
        return None