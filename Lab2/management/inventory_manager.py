from inventory.stock_item import StockItem


class InventoryManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.inventory_items = []
        self.reorder_level = 10

    def check_low_stock(self):
        low_stock = [item for item in self.inventory_items if item.quantity <= self.reorder_level]
        return low_stock

    def generate_stock_report(self):
        return "Stock report generated"