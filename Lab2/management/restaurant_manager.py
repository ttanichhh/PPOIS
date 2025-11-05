from entities.employee import Employee


class RestaurantManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.restaurant_name = ""
        self.contact_info = ""

    def generate_daily_report(self, date):
        return f"Daily report for {date}"

    def approve_special_request(self, request):
        return f"Request '{request}' approved"

    def manage_staff_schedule(self):
        return "Staff schedule updated"