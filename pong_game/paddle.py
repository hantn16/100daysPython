from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(pos)

    def up(self):
        (x, y) = self.position()
        if y < 250:
            self.goto(x, y+20)

    def down(self):
        (x, y) = self.position()
        if y > -250:
            self.goto(x, y-20)
