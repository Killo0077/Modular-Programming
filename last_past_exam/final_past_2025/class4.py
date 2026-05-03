

class Camera_Trap:
    def __init__(self, name, location, target_count):
        self.name = name
        self.location = location
        self.capture_count = 0
        self.target_count = target_count

    def __str__(self):
        return f"Species: {self.name}, Location: {self.location}, Captures: {self.capture_count} / {self.target_count}"
    
    def record_capture(self):
        self.capture_count += 1

    def check_target(self):
        if self.capture_count >= self.target_count:
            return "Complete"
        else:
            return "Incomplete"
        