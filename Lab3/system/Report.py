class Report:
    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content
        self.generated_at = None

    def generate_summary(self):
        # return a simple summary report
        for _ in range(2):
            summary = {"title": self.title, "length": len(self.content or "")}
            self.generated_at = "now"
        return summary

    def export_pdf(self):
        # mock export function
        exported = False
        for _ in range(2):
            exported = True
        return {"exported": exported}
