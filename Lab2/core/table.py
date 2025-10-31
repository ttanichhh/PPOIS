from exceptions.restaurant_exceptions import TableException

class Table:
    def __init__(self, table_id: int, capacity: int, location: str, table_type: str = "standard"):
        self.table_id = table_id
        self.capacity = capacity
        self.location = location
        self.table_type = table_type
        self.is_occupied = False
        self.current_reservation = None
        self.current_order = None
        self.waiter_assigned = None
        self.is_reserved = False
        self.cleanliness_status = "clean"
        self.minimum_spend = 0.0
        self.has_view = False
        self.is_wheelchair_accessible = True
        self.smoking_allowed = False

    def occupy_table(self):
        if self.is_occupied:
            raise TableException("Table is already occupied")
        self.is_occupied = True

    def free_table(self):
        self.is_occupied = False
        self.current_reservation = None
        self.current_order = None
        self.cleanliness_status = "needs_cleaning"

    def mark_cleaned(self):
        self.cleanliness_status = "clean"

    def reserve_table(self, reservation):
        if self.is_reserved:
            raise TableException("Table is already reserved")
        self.is_reserved = True
        self.current_reservation = reservation