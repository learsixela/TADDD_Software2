class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        return sum(self.data) / len(self.data)

class ReportPrinter:
    def print_report(self, report: Report):
        print(f"Report Data: {report.data}")
        print(f"Average: {report.calculate_statistics()}")
