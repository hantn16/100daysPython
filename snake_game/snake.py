from turtle import Turtle


class Snake():

    def __init__(self, pos=(0, 0)):
        self.segments = []
        self.length = 3
        self.create_snake(pos)
        self.head = self.segments[0]

    def create_snake(self, pos):
        start_position = [(x * -20 + pos[0], pos[1])
                          for x in range(self.length)]
        for position in start_position:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        pos = tuple(self.segments[-1].position())
        self.add_segment(pos)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_posx = self.segments[i-1].xcor()
            new_posy = self.segments[i-1].ycor()
            self.segments[i].goto(new_posx, new_posy)
        self.head.forward(20)

    def up(self):
        current_heading = self.segments[0].heading()
        if current_heading == 0 or current_heading == 180:
            self.head.setheading(90)

    def down(self):
        current_heading = self.segments[0].heading()
        if current_heading == 0 or current_heading == 180:
            self.head.setheading(270)

    def left(self):
        current_heading = self.segments[0].heading()
        if current_heading == 90 or current_heading == 270:
            self.head.setheading(180)

    def right(self):
        current_heading = self.segments[0].heading()
        if current_heading == 90 or current_heading == 270:
            self.head.setheading(0)
