from kitchen.chef import Chef


class KitchenManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.kitchen_staff = []
        self.inventory_level = ""

    def monitor_kitchen_performance(self):
        return "Kitchen performance monitored"

    def coordinate_special_orders(self):
        return "Special orders coordinated"