from support.address import Address

class Supplier:
    def __init__(self, supplier_id: int, name: str, contact_person: str, phone: str):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_person = contact_person
        self.phone = phone
        self.supplied_items = []