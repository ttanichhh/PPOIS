class StockItem:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.category = ""
        self.reorder_level = 10

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def needs_restocking(self):
        return self.quantity <= self.reorder_level