from kitchen.recipe import Recipe


class PastryChef:
    def __init__(self, chef_id, name):
        self.chef_id = chef_id
        self.name = name
        self.dessert_specialties = []

    def create_dessert(self, dessert_name):
        return f"Created dessert: {dessert_name}"

    def decorate_pastry(self, pastry):
        return f"Decorated {pastry}"