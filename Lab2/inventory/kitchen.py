class Kitchen:
    def __init__(self, kitchen_id: int, name: str, location: str):
        self.kitchen_id = kitchen_id
        self.name = name
        self.location = location
        self.chefs = []
        self.current_orders = []
        self.is_open = True

    def assign_order(self, order, chef):
        chef.current_orders.append(order)
        self.current_orders.append(order)