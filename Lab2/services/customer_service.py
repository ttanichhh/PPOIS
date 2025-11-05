from entities.customer import Customer


class CustomerService:
    def __init__(self, rep_id, name):
        self.rep_id = rep_id
        self.name = name
        self.complaints_resolved = 0

    def handle_complaint(self, complaint):
        self.complaints_resolved += 1
        return f"Complaint handled: {complaint}"

    def provide_assistance(self):
        return "Assistance provided"