from turtle import Turtle
import random

DISTANCE = 10
ANGLES = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.x_move = DISTANCE
        self.y_move = DISTANCE
        self.header = random.choice(ANGLES)
        self.speed(0)

    def move(self):
        (x, y) = self.position()
        x = x+self.x_move
        y = y+self.y_move
        self.goto(x, y)

    def ybounce(self):
        self.y_move *= -1

    def xbounce(self):
        self.x_move *= -1
