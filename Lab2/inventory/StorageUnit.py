from inventory.StockItem import StockItem


class StorageUnit:
    def __init__(self, unit_id, location):
        self.unit_id = unit_id
        self.location = location
        self.capacity = 100
        self.current_items = []

    def add_item(self, item):
        if len(self.current_items) >= self.capacity:
            return f"Storage unit {self.unit_id} is at full capacity"

        existing_items = [i.item_id for i in self.current_items]
        if item.item_id in existing_items:
            return f"Item {item.item_id} already in storage unit"

        self.current_items.append(item)
        utilization = (len(self.current_items) / self.capacity) * 100

        return f"Added {item.name} to {self.location}. Utilization: {utilization:.1f}%"

    def get_utilization(self):
        total_quantity = sum(item.quantity for item in self.current_items)
        space_used = len(self.current_items)
        utilization_percent = (space_used / self.capacity) * 100

        status = "🟢 Good" if utilization_percent < 80 else "🟡 Almost Full" if utilization_percent < 95 else "🔴 Full"

        return f"Storage {self.unit_id} - {self.location}\nItems: {space_used}/{self.capacity}\nUtilization: {utilization_percent:.1f}% {status}"