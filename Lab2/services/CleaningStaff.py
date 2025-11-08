class CleaningStaff:
    def __init__(self, staff_id, name):
        self.staff_id = staff_id
        self.name = name
        self.cleaning_schedule = ""

    def clean_area(self, area):
        area_procedures = {
            "kitchen": ["Sanitize surfaces", "Clean equipment", "Mop floors", "Dispose waste"],
            "dining": ["Wipe tables", "Vacuum carpets", "Clean windows", "Arrange chairs"],
            "restroom": ["Disinfect fixtures", "Restock supplies", "Clean mirrors", "Mop floors"]
        }

        if area.lower() not in area_procedures:
            return f"No cleaning procedure for area: {area}"

        cleaning_report = f"Cleaning {area.upper()} - {self.name}\n"
        for procedure in area_procedures[area.lower()]:
            cleaning_report += f"✓ {procedure}\n"
        cleaning_report += f"Area {area} cleaned and sanitized"
        return cleaning_report

    def restock_supplies(self):
        supply_areas = [
            "Restroom: Soap, Paper towels, Toilet paper",
            "Dining: Napkins, Condiments, Menus",
            "Kitchen: Cleaning cloths, Gloves, Sanitizer"
        ]

        restock_report = f"Supply Restocking - {self.name}\n"
        for area_supplies in supply_areas:
            restock_report += f"🔹 {area_supplies}\n"
        restock_report += "All supplies restocked and organized"
        return restock_report