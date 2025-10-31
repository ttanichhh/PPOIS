from exceptions.restaurant_exceptions import TableException

class Table:
    def __init__(self, table_id: int, capacity: int):
        self.table_id = table_id
        self.capacity = capacity
        self.is_occupied = False
        self.is_reserved = False

    def occupy_table(self):
        if self.is_occupied:
            raise TableException("Table is already occupied")
        self.is_occupied = True

    def free_table(self):
        self.is_occupied = False
        self.is_reserved = False