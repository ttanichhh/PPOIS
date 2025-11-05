class CleaningStaff:
    def __init__(self, staff_id, name):
        self.staff_id = staff_id
        self.name = name
        self.cleaning_schedule = ""

    def clean_area(self, area):
        return f"Cleaned {area}"

    def restock_supplies(self):
        return "Supplies restocked"