class StockItem:
    def __init__(self, item_id, name, quantity):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.category = ""
        self.reorder_level = 10
        self.unit_price = 0.0

    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            return "Error: Quantity cannot be negative"

        old_quantity = self.quantity
        self.quantity = new_quantity

        change = new_quantity - old_quantity
        if change > 0:
            action = f"Restocked {change} units of {self.name}"
        elif change < 0:
            action = f"Used {abs(change)} units of {self.name}"
        else:
            action = f"Quantity unchanged for {self.name}"

        status = "🟢 Adequate" if self.quantity > self.reorder_level else "🟡 Low Stock"
        return f"{action}. Current: {self.quantity} ({status})"

    def needs_restocking(self):
        if self.quantity <= self.reorder_level:
            urgency = "URGENT" if self.quantity == 0 else "Soon" if self.quantity <= 5 else "Monitor"
            return f"{self.name} needs restocking ({self.quantity} left) - {urgency}"
        return f"{self.name} stock adequate ({self.quantity} available)"