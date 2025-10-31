from inventory.supplier import Supplier

class SupplierManagement:
    def __init__(self):
        self.suppliers = []

    def add_supplier(self, supplier: Supplier):
        self.suppliers.append(supplier)

    def find_supplier_by_item(self, item_name: str) -> list:
        return [supplier for supplier in self.suppliers if item_name in supplier.supplied_items]