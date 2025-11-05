class ReportGenerator:
    def __init__(self):
        self.report_templates = []

    def generate_report(self, data, template):
        return f"Report generated using {template}"

    def export_report(self, format_type):
        return f"Report exported as {format_type}"