from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, False, "center",
                   ("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, False, "center",
                   ("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_board()

    def r_point(self):
        self.r_score += 1
        self.update_board()
