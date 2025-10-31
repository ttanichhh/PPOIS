from datetime import datetime

class Person:
    def __init__(self, person_id: int, name: str, phone: str, email: str, date_of_birth: str = None):
        self.person_id = person_id
        self.name = name
        self.phone = phone
        self.email = email
        self.date_of_birth = date_of_birth
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_contact_info(self, phone: str = None, email: str = None):
        if phone:
            self.phone = phone
        if email:
            self.email = email
        self.updated_at = datetime.now()

    def get_age(self) -> int:
        if self.date_of_birth:
            birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
            today = datetime.now()
            return today.year - birth_date.year
        return 0