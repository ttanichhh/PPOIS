from inventory.inventory import InventoryItem
from inventory.supplier import Supplier
from exceptions.restaurant_exceptions import InventoryException

class InventoryManagement:
    def __init__(self):
        self.inventory_items = []
        self.suppliers = []
        self.purchase_orders = []
        self.stock_alerts = []
        self.waste_records = []
        self.inventory_value = 0.0
        self.turnover_rate = 0.0

    def add_inventory_item(self, item: InventoryItem):
        if any(inv_item.item_id == item.item_id for inv_item in self.inventory_items):
            raise InventoryException("Item ID already exists")
        self.inventory_items.append(item)
        self.update_inventory_value()

    def remove_inventory_item(self, item_id: int):
        item = self.find_item_by_id(item_id)
        if item:
            self.inventory_items.remove(item)
            self.update_inventory_value()

    def find_item_by_id(self, item_id: int) -> InventoryItem:
        for item in self.inventory_items:
            if item.item_id == item_id:
                return item
        return None

    def update_stock_level(self, item_id: int, new_quantity: int):
        item = self.find_item_by_id(item_id)
        if item:
            item.update_quantity(new_quantity)
            self.check_stock_alerts(item)
            self.update_inventory_value()

    def check_stock_alerts(self, item: InventoryItem):
        if item.needs_restocking():
            self.stock_alerts.append({
                "item_id": item.item_id,
                "item_name": item.name,
                "current_stock": item.quantity,
                "reorder_level": item.reorder_level,
                "alert_date": "2024-01-20"
            })

    def update_inventory_value(self):
        self.inventory_value = sum(item.get_total_value() for item in self.inventory_items)

    def generate_purchase_order(self, supplier: Supplier, items: list):
        po_number = f"PO-{len(self.purchase_orders) + 1:06d}"
        purchase_order = {
            "po_number": po_number,
            "supplier": supplier.name,
            "items": items,
            "total_amount": sum(item['quantity'] * item['cost'] for item in items),
            "order_date": "2024-01-20",
            "status": "pending"
        }
        self.purchase_orders.append(purchase_order)
        return purchase_order

    def record_waste(self, item: InventoryItem, quantity: int, reason: str):
        waste_cost = quantity * item.cost_per_unit
        self.waste_records.append({
            "item_id": item.item_id,
            "item_name": item.name,
            "quantity": quantity,
            "cost": waste_cost,
            "reason": reason,
            "date": "2024-01-20"
        })