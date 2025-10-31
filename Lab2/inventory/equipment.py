class CookingEquipment:
    def __init__(self, equipment_id: int, name: str, equipment_type: str):
        self.equipment_id = equipment_id
        self.name = name
        self.equipment_type = equipment_type
        self.status = "operational"