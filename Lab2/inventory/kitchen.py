from exceptions.restaurant_exceptions import KitchenException  # 🔹 ИСПРАВЛЕНО


class Kitchen:
    def __init__(self, kitchen_id: int, name: str, location: str):
        self.kitchen_id = kitchen_id
        self.name = name
        self.location = location
        self.chefs = []
        self.current_orders = []
        self.equipment = []
        self.stations = []
        self.inventory = []
        self.is_open = True
        self.temperature_zones = {}
        self.safety_rating = 5.0
        self.cleaning_schedule = []

    def assign_order(self, order, chef):
        chef.current_orders.append(order)
        self.current_orders.append(order)

    def add_equipment(self, equipment_name: str):
        self.equipment.append(equipment_name)

    def close_kitchen(self):
        self.is_open = False

    def open_kitchen(self):
        self.is_open = True