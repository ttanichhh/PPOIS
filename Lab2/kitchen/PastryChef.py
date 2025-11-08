from kitchen.Recipe import Recipe


class PastryChef:
    def __init__(self, chef_id, name):
        self.chef_id = chef_id
        self.name = name
        self.dessert_specialties = []

    def create_dessert(self, dessert_name):
        dessert_types = {
            "cake": ["Bake layers", "Prepare frosting", "Assemble and decorate"],
            "pastry": ["Prepare dough", "Add filling", "Bake to perfection"],
            "chocolate": ["Temper chocolate", "Create molds", "Add decorations"]
        }

        dessert_type = "pastry"
        for dtype in dessert_types:
            if dtype in dessert_name.lower():
                dessert_type = dtype
                break

        creation_process = f"Creating {dessert_name}\n"
        for step in dessert_types[dessert_type]:
            creation_process += f"🎂 {step}\n"
        creation_process += "Ready to serve!"
        return creation_process

    def manage_dessert_inventory(self):
        inventory_items = ["Flour", "Sugar", "Butter", "Eggs", "Chocolate", "Fruits"]
        stock_levels = [85, 90, 75, 95, 80, 70]

        inventory_report = f"Dessert Inventory - Chef {self.name}\n"
        for item, level in zip(inventory_items, stock_levels):
            status = "🟢 Good" if level > 70 else "🟡 Low"
            inventory_report += f"{item}: {level}% {status}\n"
        return inventory_report