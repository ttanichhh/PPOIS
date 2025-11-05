from kitchen.dish import Dish


class LineCook:
    def __init__(self, cook_id, name):
        self.cook_id = cook_id
        self.name = name
        self.station = ""
        self.specialties = []

    def prepare_dish(self, dish):
        return f"Preparing {dish.name}"

    def maintain_station(self):
        return "Station maintained"