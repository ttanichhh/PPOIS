from entities.menu_item import MenuItem


class MenuManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.menu_items = []

    def add_menu_item(self, item):
        self.menu_items.append(item)
        return f"Added {item.name} to menu"

    def update_menu_prices(self, increase_percent):
        for item in self.menu_items:
            item.price *= (1 + increase_percent / 100)