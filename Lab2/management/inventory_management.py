from inventory.inventory import InventoryItem
from inventory.supplier import Supplier
from exceptions.restaurant_exceptions import InventoryException

class InventoryManagement:
    def __init__(self):
        self.inventory_items = []
        self.suppliers = []

    def add_inventory_item(self, item: InventoryItem):
        if any(inv_item.item_id == item.item_id for inv_item in self.inventory_items):
            raise InventoryException("Item ID already exists")
        self.inventory_items.append(item)

    def find_item_by_id(self, item_id: int) -> InventoryItem:
        for item in self.inventory_items:
            if item.item_id == item_id:
                return item
        return None

    def update_stock_level(self, item_id: int, new_quantity: int):
        item = self.find_item_by_id(item_id)
        if item:
            item.update_quantity(new_quantity)