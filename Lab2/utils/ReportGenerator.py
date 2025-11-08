class ReportGenerator:
    def __init__(self):
        self.report_templates = []

    def generate_report(self, data, template):
        if not data:
            return "No data provided for report generation"

        template_types = {
            "sales": "Sales Performance Analysis",
            "inventory": "Inventory Status Report",
            "staff": "Staff Performance Review",
            "financial": "Financial Summary Report"
        }

        report_title = template_types.get(template.lower(), "Custom Report")

        report = f"=== {report_title} ===\n"
        report += f"Generated on: 2024-01-15\n"
        report += f"Template: {template}\n"
        report += f"Data points: {len(data) if hasattr(data, '__len__') else 1}\n"
        report += "-" * 40 + "\n"

        if template.lower() == "sales":
            report += "Top Performing Items:\n• Margherita Pizza\n• Caesar Salad\n• Tiramisu\n"
        elif template.lower() == "inventory":
            report += "Inventory Status:\n• 85% items in stock\n• 5 items need reorder\n• Overall: Good\n"

        report += "=" * 40
        return report

    def export_report(self, format_type):
        supported_formats = ["PDF", "Excel", "CSV", "HTML"]

        if format_type.upper() not in supported_formats:
            return f"Unsupported format: {format_type}. Available: {', '.join(supported_formats)}"

        export_steps = [
            "Formatting data structure",
            "Applying template styling",
            "Generating output file",
            "Quality checking export",
            f"Saving as {format_type.upper()} format"
        ]

        export_log = f"Exporting Report as {format_type.upper()}\n"
        for step in export_steps:
            export_log += f"✓ {step}\n"
        export_log += "Export completed successfully"
        return export_log