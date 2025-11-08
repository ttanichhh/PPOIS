from inventory.StockItem import StockItem


class InventoryTracker:
    def __init__(self, tracker_id):
        self.tracker_id = tracker_id
        self.stock_items = []
        self.last_updated = ""

    def add_stock_item(self, item):
        existing_ids = [i.item_id for i in self.stock_items]
        if item.item_id in existing_ids:
            return f"Item ID {item.item_id} already exists in tracker"

        self.stock_items.append(item)

        category_count = {}
        for stock_item in self.stock_items:
            cat = stock_item.category if stock_item.category else "Uncategorized"
            category_count[cat] = category_count.get(cat, 0) + 1

        return f"Added {item.name} to inventory. Now tracking {len(self.stock_items)} items across {len(category_count)} categories"

    def find_low_stock(self):
        low_stock_items = [item for item in self.stock_items if item.quantity <= item.reorder_level]
        critical_items = [item for item in low_stock_items if item.quantity == 0]

        if not low_stock_items:
            return "All inventory levels are adequate"

        report = f"Inventory Alert - {len(low_stock_items)} items need attention\n"
        if critical_items:
            report += "CRITICAL (Out of stock):\n"
            for item in critical_items:
                report += f"🚨 {item.name} - OUT OF STOCK\n"

        report += "Low Stock:\n"
        for item in [i for i in low_stock_items if i.quantity > 0]:
            report += f"⚠️  {item.name} - {item.quantity} left (reorder at {item.reorder_level})\n"

        return report