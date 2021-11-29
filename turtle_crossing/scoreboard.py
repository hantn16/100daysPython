from turtle import Turtle
FONT1 = ("Courier", 24, "normal")
FONT2 = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.pencolor("black")
        self.goto(-270, 250)
        self.write_score()
        self.hideturtle()

    def level_up(self):
        self.level += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', font=FONT1, align="left")

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(
            arg=f'GAME OVER\nYour Score: {self.level}', font=FONT1, align="center")
