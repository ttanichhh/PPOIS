class Barista:
    def __init__(self, barista_id, name):
        self.barista_id = barista_id
        self.name = name
        self.coffee_specialties = []

    def prepare_coffee(self, coffee_type):
        return f"Preparing {coffee_type}"

    def maintain_equipment(self):
        return "Coffee equipment maintained"