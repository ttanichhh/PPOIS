from core.table import Table

class TableManagementService:
    def __init__(self):
        self.table_assignments = {}

    @staticmethod
    def assign_table_to_group(tables: list, group_size: int) -> Table:
        suitable_tables = [table for table in tables
                           if table.capacity >= group_size and not table.is_occupied]
        if suitable_tables:
            return min(suitable_tables, key=lambda x: x.capacity)
        return None