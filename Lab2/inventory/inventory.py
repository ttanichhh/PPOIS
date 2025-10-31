from exceptions.restaurant_exceptions import InventoryException

class InventoryItem:
    def __init__(self, item_id: int, name: str, category: str, quantity: int,
                 unit: str, reorder_level: int, cost_per_unit: float):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit = unit
        self.reorder_level = reorder_level
        self.cost_per_unit = cost_per_unit
        self.supplier_id = None
        self.storage_location = ""
        self.expiry_date = None
        self.batch_number = ""
        self.min_stock_level = 0
        self.max_stock_level = 1000
        self.last_restocked = None

    def update_quantity(self, new_quantity: int):
        if new_quantity < 0:
            raise InventoryException("Quantity cannot be negative")
        self.quantity = new_quantity

    def needs_restocking(self) -> bool:
        return self.quantity <= self.reorder_level

    def get_total_value(self) -> float:
        return self.quantity * self.cost_per_unit

class Supplier:
    def __init__(self, supplier_id: int, name: str, contact_person: str,
                 phone: str, email: str, address: str):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_person = contact_person
        self.phone = phone
        self.email = email
        self.address = address
        self.supplied_items = []
        self.rating = 0.0
        self.payment_terms = ""
        self.lead_time_days = 7
        self.is_active = True

    def add_supplied_item(self, item_name: str):
        self.supplied_items.append(item_name)

    def update_rating(self, new_rating: float):
        self.rating = new_rating