def format_report(func):
    def wrapper(*args, **kwargs):
        print("=" * 40)
        func(*args, **kwargs)
        print("=" * 40)
    return wrapper


class ReportGenerator:
    templates = {
        "default": "Standard Report",
        "executive": "Executive Summary"
    }

    def __init__(self, title, content, template_key="default"):
        self.title = title
        self.content = content
        self.template_key = template_key

    @classmethod
    def add_template(cls, key, template_name):
        cls.templates[key] = template_name

    def __str__(self):
        template_name = self.templates.get(self.template_key, "Custom")
        return f"Title: {self.title}\nTemplate: {template_name}\nContent: {self.content}"

    @format_report
    def generate_report(self):
        print(str(self))


report1 = ReportGenerator("Sales Report", "Sales went up by 15% this month.", "executive")
report1.generate_report()

ReportGenerator.add_template("academic", "Academic Format")
report2 = ReportGenerator("Research Paper", "Data analysis complete.", "academic")
report2.generate_report()