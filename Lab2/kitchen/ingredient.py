from inventory.stock_item import StockItem


class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.unit = ""
        self.quality = ""

    def check_quality(self):
        return f"Quality of {self.name}: {self.quality}"