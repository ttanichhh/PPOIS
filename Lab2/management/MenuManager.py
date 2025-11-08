from entities.MenuItem import MenuItem

class MenuManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.menu_items = []

    def add_menu_item(self, item):
        existing_ids = [i.item_id for i in self.menu_items]
        if item.item_id in existing_ids:
            return f"Item ID {item.item_id} already exists in menu"

        self.menu_items.append(item)

        menu_categories = {}
        for menu_item in self.menu_items:
            cat = menu_item.category if menu_item.category else "Uncategorized"
            menu_categories[cat] = menu_categories.get(cat, 0) + 1

        return f"Added {item.name} to menu. Now {len(self.menu_items)} items across {len(menu_categories)} categories"

    def update_menu_prices(self, increase_percent):
        if increase_percent < -50 or increase_percent > 100:
            return "Price change must be between -50% and +100%"

        total_increase = 0
        for item in self.menu_items:
            old_price = item.price
            item.price *= (1 + increase_percent / 100)
            total_increase += item.price - old_price

        return f"Updated {len(self.menu_items)} items. Total value increase: ${total_increase:.2f}"