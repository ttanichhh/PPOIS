class Table:
    def __init__(self, table_id, capacity):
        self.table_id = table_id
        self.capacity = capacity
        self.is_occupied = False
        self.location = ""

    def occupy_table(self):
        self.is_occupied = True

    def free_table(self):
        self.is_occupied = False

    def can_accommodate(self, guests):
        return guests <= self.capacity