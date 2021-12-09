from datetime import datetime


class Workout():
    def __init__(self, name, duration, calories):
        self.date = datetime.now().strftime("%d/%m/%Y")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.exercise = name,
        self.duration = duration,
        self.calories = calories
