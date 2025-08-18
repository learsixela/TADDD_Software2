class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        return sum(self.data) / len(self.data)

    def print_report(self):
        print(f"Report Data: {self.data}")
        print(f"Average: {self.calculate_statistics()}")
