from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time
import random

screen = Screen()
screen.setup(800, 600)
screen.title("My Pong Game")
screen.bgcolor("black")

# screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
sb = ScoreBoard()
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if abs(ball.ycor()) >= 290:
        ball.ybounce()
    if ball.xcor() == 330 and abs(ball.ycor()-right_paddle.ycor()) <= 50 or ball.xcor() == -330 and abs(ball.ycor()-left_paddle.ycor()) <= 50:
        ball.xbounce()
    if ball.xcor() >= 390:
        ball.reset()
        sb.l_point()
    if ball.xcor() <= -390:
        ball.reset()
        sb.r_point()


screen.exitonclick()
