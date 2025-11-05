from kitchen.line_cook import LineCook


class KitchenStation:
    def __init__(self, station_id, name):
        self.station_id = station_id
        self.name = name
        self.equipment = []
        self.assigned_cook = None

    def assign_cook(self, cook):
        self.assigned_cook = cook
        return f"Assigned {cook.name} to {self.name}"

    def get_station_status(self):
        return f"Station {self.name} - Cook: {self.assigned_cook.name if self.assigned_cook else 'None'}"