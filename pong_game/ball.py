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
        self.move_speed = 0.1

    def move(self):
        (x, y) = self.position()
        x = x+self.x_move
        y = y+self.y_move
        self.goto(x, y)

    def ybounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def xbounce(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
