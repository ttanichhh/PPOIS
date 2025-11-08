from inventory.StockItem import StockItem


class InventoryManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.inventory_items = []
        self.reorder_level = 10

    def check_low_stock(self):
        low_stock_items = []
        for item in self.inventory_items:
            if item.quantity <= self.reorder_level:
                low_stock_items.append(item)

        if low_stock_items:
            report = f"Low stock alert - {len(low_stock_items)} items:\n"
            for item in low_stock_items:
                report += f"- {item.name}: {item.quantity} left\n"
            return report
        return "All inventory levels are adequate"

    def generate_stock_report(self):
        total_items = len(self.inventory_items)
        total_value = sum(item.quantity * item.unit_price for item in self.inventory_items)

        report = f"Inventory Report - {self.name}\n"
        report += f"Total items: {total_items}\n"
        report += f"Total value: ${total_value:.2f}\n"
        report += f"Items monitored: {len(self.inventory_items)}"
        return report