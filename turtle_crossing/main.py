from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time
GAME_SPEED = 0.1


def game_start():
    player = Player()
    car_manager = CarManager()
    scoreboard = ScoreBoard()
    scr.onkeypress(player.move_up, "Up")
    scr.onkeypress(player.move_down, "Down")

    game_is_on = True

    while game_is_on:
        time.sleep(GAME_SPEED)
        car_manager.create_car()
        if not car_manager.move_cars(player.xcor(), player.ycor()):
            game_is_on = False
            scoreboard.game_over()
        if player.win:
            player.go_to_start()
            car_manager.level_up()
            scoreboard.level_up()
        scr.update()


scr = Screen()
scr.setup(width=600, height=600)
scr.title("My Turtle Crossing Game v1")
scr.tracer(0)
scr.listen()
game_start()


scr.exitonclick()
