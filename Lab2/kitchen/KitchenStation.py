from kitchen.LineCook import LineCook


class KitchenStation:
    def __init__(self, station_id, name):
        self.station_id = station_id
        self.name = name
        self.equipment = []
        self.assigned_cook = None

    def assign_cook(self, cook):
        if self.assigned_cook:
            previous_cook = self.assigned_cook.name
        else:
            previous_cook = "None"

        self.assigned_cook = cook

        station_requirements = {
            "grill": "Grill master certification",
            "saute": "Sauce expertise",
            "pastry": "Baking skills"
        }

        requirement = station_requirements.get(self.name.lower(), "Basic training")
        return f"Assigned {cook.name} to {self.name} (was: {previous_cook}). Requirement: {requirement}"

    def get_station_status(self):
        equipment_status = "All equipment operational"
        if any("oven" in eq.lower() for eq in self.equipment):
            equipment_status = "Oven preheating, other equipment ready"

        cook_info = self.assigned_cook.name if self.assigned_cook else "No cook assigned"
        status = f"Station {self.name} (ID: {self.station_id})\n"
        status += f"Cook: {cook_info}\n"
        status += f"Equipment: {equipment_status}\n"
        status += f"Tools: {len(self.equipment)} items"
        return status