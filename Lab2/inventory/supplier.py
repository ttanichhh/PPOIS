class Supplier:
    def __init__(self, supplier_id, name):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = ""
        self.products = []

    def place_order(self, items):
        return f"Order placed with {self.name}"

    def get_supplier_info(self):
        return f"{self.name} ({self.contact_info})"