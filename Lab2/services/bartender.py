from entities.order import Order


class Bartender:
    def __init__(self, bartender_id, name):
        self.bartender_id = bartender_id
        self.name = name
        self.specialty_drinks = []

    def prepare_drink(self, drink_name):
        return f"Preparing {drink_name}"

    def manage_bar_stock(self):
        return "Bar stock managed"