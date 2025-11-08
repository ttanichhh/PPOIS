class Table:
    def __init__(self, table_id, capacity):
        self.table_id = table_id
        self.capacity = capacity
        self.is_occupied = False
        self.location = ""

    def occupy_table(self):
        if self.is_occupied:
            return f"Table {self.table_id} is already occupied"

        self.is_occupied = True
        return f"Table {self.table_id} is now occupied"

    def free_table(self):
        if not self.is_occupied:
            return f"Table {self.table_id} is already free"

        self.is_occupied = False
        return f"Table {self.table_id} is now available"

    def can_accommodate(self, guests):
        if guests > self.capacity:
            return f"Cannot accommodate {guests} guests (max: {self.capacity})"
        elif guests <= 0:
            return "Invalid number of guests"
        else:
            return f"Can accommodate {guests} guests at table {self.table_id}"