class ClassName:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.total = 0

    def __str__(self):
        return f"{self.name:<10}{self.value:<10}{self.total:<10}"

    def add_value(self, amount):
        self.total += amount

    def remaining(self):
        remaining = self.value - self.total
        if remaining < 0:
            return 0
        return remaining