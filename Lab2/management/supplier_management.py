from inventory.supplier import Supplier

class SupplierManagement:
    def __init__(self):
        self.suppliers = []
        self.purchase_orders = []
        self.contracts = []
        self.performance_metrics = {}
        self.supplier_evaluations = []

    def add_supplier(self, supplier: Supplier):
        self.suppliers.append(supplier)

    def find_supplier_by_item(self, item_name: str) -> list:
        return [supplier for supplier in self.suppliers if item_name in supplier.supplied_items]

    def evaluate_supplier(self, supplier: Supplier, rating: float, comments: str):
        evaluation = {
            "supplier_id": supplier.supplier_id,
            "rating": rating,
            "comments": comments,
            "evaluation_date": "2024-01-20"
        }
        self.supplier_evaluations.append(evaluation)
        supplier.rating = rating

    def generate_supplier_report(self) -> dict:
        total_suppliers = len(self.suppliers)
        active_suppliers = len([s for s in self.suppliers if s.is_active])
        avg_rating = sum(s.rating for s in self.suppliers) / total_suppliers if total_suppliers > 0 else 0

        return {
            "total_suppliers": total_suppliers,
            "active_suppliers": active_suppliers,
            "average_rating": avg_rating,
            "top_suppliers": sorted(self.suppliers, key=lambda x: x.rating, reverse=True)[:5]
        }