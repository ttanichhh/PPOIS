class Supplier:
    def __init__(self, supplier_id, name):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = ""
        self.products = []

    def place_order(self, items):
        if not items:
            return "No items to order"

        order_total = len(items) * 25.0  # Simulated average item cost
        delivery_time = "2-3 days" if len(items) <= 10 else "3-5 days"

        order_summary = f"Order Placed with {self.name}\n"
        order_summary += f"Items ordered: {len(items)}\n"
        order_summary += f"Estimated cost: ${order_total:.2f}\n"
        order_summary += f"Delivery time: {delivery_time}\n"
        order_summary += f"Contact: {self.contact_info}"
        return order_summary

    def get_supplier_info(self):
        product_categories = {}
        for product in self.products:
            category = product.split()[0] if ' ' in product else "General"
            product_categories[category] = product_categories.get(category, 0) + 1

        categories_info = ", ".join([f"{cat}({count})" for cat, count in product_categories.items()])

        info = f"Supplier: {self.name}\n"
        info += f"ID: {self.supplier_id}\n"
        info += f"Contact: {self.contact_info}\n"
        info += f"Products: {categories_info}"
        return info