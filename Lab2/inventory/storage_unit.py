from inventory.stock_item import StockItem


class StorageUnit:
    def __init__(self, unit_id, location):
        self.unit_id = unit_id
        self.location = location
        self.capacity = 100
        self.current_items = []

    def add_item(self, item):
        if len(self.current_items) < self.capacity:
            self.current_items.append(item)
            return True
        return False

    def get_utilization(self):
        return len(self.current_items) / self.capacity * 100