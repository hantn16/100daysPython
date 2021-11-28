from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.pencolor('white')
        self.penup()
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False,
                   "center", ('Courier', 24, 'normal'))

    def write_score(self):
        self.clear()
        self.pendown()
        self.write(f'Score: {self.score}', False,
                   "center", ('Arial', 18, 'normal'))
