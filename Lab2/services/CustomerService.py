from entities.Customer import Customer


class CustomerService:
    def __init__(self, rep_id, name):
        self.rep_id = rep_id
        self.name = name
        self.complaints_resolved = 0
        self.customer_satisfaction = 0.0

    def handle_complaint(self, complaint):
        complaint_keywords = {
            "cold": "We apologize for the temperature issue",
            "slow": "We're addressing our service speed",
            "wrong": "We'll correct your order immediately",
            "dirty": "We'll ensure cleanliness standards",
            "rude": "We'll address staff behavior"
        }

        response = f"Complaint received: '{complaint}'\n"
        for keyword, apology in complaint_keywords.items():
            if keyword in complaint.lower():
                response += f"Action: {apology}\n"
                break
        else:
            response += "Action: We'll investigate this matter\n"

        self.complaints_resolved += 1
        response += f"Complaint #{self.complaints_resolved} resolved by {self.name}"
        return response

    def provide_assistance(self):
        assistance_options = [
            "Menu recommendations and explanations",
            "Allergy and dietary restriction information",
            "Special occasion arrangements",
            "Billing and payment assistance",
            "Feedback and complaint resolution"
        ]

        assistance_menu = f"Customer Service - {self.name}\n"
        assistance_menu += "How can I assist you today?\n"
        for i, option in enumerate(assistance_options, 1):
            assistance_menu += f"{i}. {option}\n"
        assistance_menu += "Please let me know how I can help!"
        return assistance_menu