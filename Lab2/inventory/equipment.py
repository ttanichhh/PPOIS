class CookingEquipment:
    def __init__(self, equipment_id: int, name: str, equipment_type: str, status: str):
        self.equipment_id = equipment_id
        self.name = name
        self.equipment_type = equipment_type
        self.status = status
        self.last_maintenance = ""
        self.next_maintenance = ""
        self.energy_consumption = 0.0
        self.capacity = ""
        self.location = ""
        self.manufacturer = ""
        self.purchase_date = ""

    def schedule_maintenance(self, date: str):
        self.next_maintenance = date

    def mark_maintenance_completed(self):
        self.last_maintenance = "2024-01-20"
        self.status = "operational"