from kitchen.Dish import Dish


class LineCook:
    def __init__(self, cook_id, name):
        self.cook_id = cook_id
        self.name = name
        self.station = ""
        self.specialties = []

    def prepare_dish(self, dish):
        prep_steps = [
            f"Gather ingredients for {dish.name}",
            "Prepare cooking station and equipment",
            "Follow recipe specifications",
            "Monitor cooking temperature and time",
            "Plate dish according to standards"
        ]

        preparation_log = f"Preparing {dish.name}\n"
        for step in prep_steps:
            preparation_log += f"→ {step}\n"
        preparation_log += f"Estimated time: {dish.calculate_prep_time()} minutes"
        return preparation_log

    def maintain_station_cleanliness(self):
        cleaning_tasks = [
            "Sanitize all surfaces",
            "Clean and organize tools",
            "Restock ingredients and supplies",
            "Check equipment functionality",
            "Dispose of waste properly"
        ]

        maintenance_report = f"Station Maintenance - {self.station}\n"
        for task in cleaning_tasks:
            maintenance_report += f"✓ {task}\n"
        maintenance_report += "Station ready for service"
        return maintenance_report