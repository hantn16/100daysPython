from turtle import Turtle

FONT = ('Courier', 18, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_highscore()
        self.color('white')
        self.pencolor('white')
        self.penup()
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()

    def add_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore()
        self.write_score()

    def update_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def get_highscore(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def reset(self):
        self.score = 0
        self.get_highscore()
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', False,
    #                "center", FONT)

    def write_score(self):
        self.clear()
        self.write(
            arg=f'Score: {self.score} High Score: {self.high_score}', font=FONT, align='center')
