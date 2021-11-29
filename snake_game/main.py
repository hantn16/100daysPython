from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake((-20, 0))
food = Food()
board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 10:
        snake.extend()
        food.refresh()
        board.add_score()
    if snake.head.xcor() > 390 or snake.head.ycor() > 290 or snake.head.xcor() < -390 or snake.head.ycor() < -290:
        board.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            board.reset()
            snake.reset()


screen.exitonclick()
