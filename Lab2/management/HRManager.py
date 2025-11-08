from entities.Employee import Employee

class HRManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.employees = []
        self.hiring_schedule = ""

    def hire_employee(self, employee):
        if any(e.employee_id == employee.employee_id for e in self.employees):
            return f"Employee ID {employee.employee_id} already exists"

        self.employees.append(employee)
        welcome_package = f"Welcome {employee.name}!\n"
        welcome_package += f"Position: {employee.position}\n"
        welcome_package += f"Orientation scheduled for next Monday"
        return welcome_package

    def conduct_interview(self, candidate):
        questions = [
            "Tell us about your experience",
            "Why do you want to work here?",
            "How do you handle pressure?"
        ]

        interview_report = f"Interview with {candidate}\n"
        interview_report += "Questions asked:\n"
        for i, question in enumerate(questions, 1):
            interview_report += f"{i}. {question}\n"
        interview_report += "Evaluation: Pending review"
        return interview_report