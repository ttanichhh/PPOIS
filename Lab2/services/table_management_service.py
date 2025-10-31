from core.table import Table
from support.reservation import Reservation

class TableManagementService:
    def __init__(self):
        self.table_assignments = {}
        self.table_status_history = []
        self.cleaning_schedule = []
        self.table_configurations = []

    @staticmethod
    def assign_table_to_group(tables: list, group_size: int) -> Table:
        suitable_tables = [table for table in tables
                           if table.capacity >= group_size and not table.is_occupied]
        if suitable_tables:
            return min(suitable_tables, key=lambda x: x.capacity)
        return None

    @staticmethod
    def combine_tables(tables: list) -> bool:
        # Logic to combine adjacent tables
        if len(tables) >= 2:
            return True
        return False

    @staticmethod
    def get_table_utilization(tables: list, date: str) -> dict:
        occupied_count = len([table for table in tables if table.is_occupied])
        reserved_count = len([table for table in tables if table.is_reserved])
        total_tables = len(tables)

        return {
            "date": date,
            "total_tables": total_tables,
            "occupied_tables": occupied_count,
            "reserved_tables": reserved_count,
            "utilization_rate": ((occupied_count + reserved_count) / total_tables) * 100
        }

    def schedule_cleaning(self, table: Table, cleaning_time: str):
        self.cleaning_schedule.append({
            "table_id": table.table_id,
            "cleaning_time": cleaning_time,
            "status": "scheduled"
        })