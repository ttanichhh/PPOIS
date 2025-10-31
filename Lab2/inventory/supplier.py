from support.address import Address

class Supplier:
    def __init__(self, supplier_id: int, name: str, contact_person: str, phone: str, email: str, address: Address):
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
        self.contract_start_date = ""
        self.contract_end_date = ""
        self.min_order_amount = 0.0

    def add_supplied_item(self, item_name: str):
        self.supplied_items.append(item_name)

    def update_rating(self, new_rating: float):
        self.rating = new_rating

    @staticmethod
    def is_contract_valid() -> bool:
        return True