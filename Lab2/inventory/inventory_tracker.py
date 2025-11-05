from inventory.stock_item import StockItem


class InventoryTracker:
    def __init__(self, tracker_id):
        self.tracker_id = tracker_id
        self.stock_items = []
        self.last_updated = ""

    def add_stock_item(self, item):
        self.stock_items.append(item)

    def find_low_stock(self):
        return [item for item in self.stock_items if item.needs_restocking()]