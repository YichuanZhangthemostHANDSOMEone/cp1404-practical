class Project:
    """Create a project class"""

    def __init__(self, name, start_date, priority, cost_estimate, percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage = percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.percentage}%"

    def is_completed(self):
        return self.percentage == "100"

    def __lt__(self, other):
        return self.start_date < other.start_date

    def __le__(self, other):
        return self.priority <= other.priority
