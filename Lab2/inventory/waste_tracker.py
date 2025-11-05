class WasteTracker:
    def __init__(self, tracker_id):
        self.tracker_id = tracker_id
        self.waste_records = []
        self.total_waste = 0.0

    def record_waste(self, item, amount):
        self.waste_records.append((item, amount))
        self.total_waste += amount

    def get_waste_report(self):
        return f"Total waste: {self.total_waste}"