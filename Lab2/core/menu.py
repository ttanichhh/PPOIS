from exceptions.restaurant_exceptions import MenuException

class Menu:
    def __init__(self, menu_id: int, name: str):
        self.menu_id = menu_id
        self.name = name
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def get_category_by_id(self, category_id: int):
        for category in self.categories:
            if category.category_id == category_id:
                return category
        return None

class MenuCategory:
    def __init__(self, category_id: int, name: str):
        self.category_id = category_id
        self.name = name
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

class MenuItem:
    def __init__(self, item_id: int, name: str, price: float, category: str):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

    def get_item_details(self):
        return f"{self.name} - ${self.price}"