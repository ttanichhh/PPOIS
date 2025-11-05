from entities.employee import Employee


class HRManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.employees = []
        self.hiring_schedule = ""

    def hire_employee(self, employee):
        self.employees.append(employee)
        return f"Hired {employee.name}"

    def conduct_interview(self, candidate):
        return f"Interviewed {candidate}"