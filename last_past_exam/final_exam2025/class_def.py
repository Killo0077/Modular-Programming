
class Runner_Details:
    def __init__(self,name, goal):
        self.name = name
        self.goal = goal
        self.total_run = 0

    def __str__(self):
        return f"{self.name:<10}{self.goal:<10}{self.total_run:<10}{self.remaining_km()}"
    
    
    def add_run(self, distance):
        self.total_run += distance

    def remaining_km(self):
        remaining = self.goal - self.total_run
        if remaining < 0:
            return 0 
        return remaining