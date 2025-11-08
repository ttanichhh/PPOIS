class Barista:
    def __init__(self, barista_id, name):
        self.barista_id = barista_id
        self.name = name
        self.coffee_specialties = []

    def prepare_coffee(self, coffee_type):
        coffee_preparations = {
            "espresso": ["Grind beans", "Tamp grounds", "Extract shot", "Serve immediately"],
            "cappuccino": ["Prepare espresso", "Steam milk", "Foam milk", "Combine layers"],
            "latte": ["Make espresso", "Steam milk", "Pour milk art", "Add finishing touch"],
            "americano": ["Brew espresso", "Add hot water", "Stir gently", "Serve hot"]
        }

        if coffee_type.lower() not in coffee_preparations:
            return f"Sorry, we don't serve {coffee_type}"

        preparation = f"Preparing {coffee_type.title()} - {self.name}\n"
        for step in coffee_preparations[coffee_type.lower()]:
            preparation += f"☕ {step}\n"
        preparation += "Enjoy your coffee!"
        return preparation

    def maintain_equipment(self):
        maintenance_tasks = [
            "Clean espresso machine group heads",
            "Descale coffee machine",
            "Calibrate grinder settings",
            "Sanitize steam wands",
            "Check water filtration system"
        ]

        maintenance_log = f"Coffee Equipment Maintenance\n"
        maintenance_log += f"Barista: {self.name}\n"
        for task in maintenance_tasks:
            maintenance_log += f"🔧 {task}\n"
        maintenance_log += "All equipment in optimal condition"
        return maintenance_log