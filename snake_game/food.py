from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('aqua')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.resizemode('user')
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-14, 14)*20,
                  random.randint(-14, 14)*20)
