from entities.Employee import Employee


class RestaurantManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.restaurant_name = ""
        self.contact_info = ""

    def generate_daily_report(self, date):
        revenue = 1500.75
        customers_served = 45
        popular_item = "Margherita Pizza"

        report = f"Daily Report - {date}\n"
        report += f"Restaurant: {self.restaurant_name}\n"
        report += f"Revenue: ${revenue:.2f}\n"
        report += f"Customers served: {customers_served}\n"
        report += f"Most popular: {popular_item}"
        return report

    def approve_special_request(self, request):
        special_requests = {
            "birthday": "Approved with complimentary dessert",
            "anniversary": "Approved with flowers and special seating",
            "VIP": "Approved with premium service"
        }
        if request.lower() in special_requests:
            return special_requests[request.lower()]
        return f"Special request '{request}' reviewed and approved"