from turtle import Turtle
STARTING_POSITION = (0, -290)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 290


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.win = False
        self.color("red")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.win = False

    def move_up(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() >= FINISH_LINE_Y:
            self.win = True

    def move_down(self):
        if self.ycor() > -280:
            self.backward(MOVE_DISTANCE)
