class QualityManager:
    def __init__(self, manager_id, name):
        self.manager_id = manager_id
        self.name = name
        self.quality_standards = ""
        self.inspection_schedule = ""

    def conduct_quality_check(self):
        return "Quality check conducted"

    def generate_quality_report(self):
        return "Quality report generated"