from kitchen.Chef import Chef

class KitchenManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.kitchen_staff = []
        self.inventory_level = ""

    def monitor_kitchen_performance(self):
        orders_completed = 78
        avg_prep_time = "12.5 minutes"
        quality_score = "94%"

        report = f"Kitchen Performance Report\n"
        report += f"Manager: {self.name}\n"
        report += f"Orders completed: {orders_completed}\n"
        report += f"Avg prep time: {avg_prep_time}\n"
        report += f"Quality score: {quality_score}"
        return report

    def coordinate_special_orders(self):
        special_orders = ["gluten-free", "vegan", "allergy-sensitive"]
        coordination_msg = f"Coordinating {len(special_orders)} special orders:\n"
        for order in special_orders:
            coordination_msg += f"- {order} preparation\n"
        coordination_msg += "All special orders assigned to trained staff"
        return coordination_msg