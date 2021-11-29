import random
import time
from turtle import Turtle
COLORS = ["red", "blue", "orange", "green", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_speed = MOVE_INCREMENT

    def create_car(self):
        if random.randint(0, 2) == 0:
            car = Car()
            self.cars.append(car)

    def move_cars(self, player_x, player_y):
        for car in self.cars:
            car.backward(self.cars_speed)
            if car.distance(player_x, player_y) < 20:
                return False
            if car.xcor() <= -320:
                self.cars.remove(car)
                del car

        return True

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.randrange(-250, 250, STARTING_MOVE_DISTANCE))
