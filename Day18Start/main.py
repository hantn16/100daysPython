from turtle import Turtle, Screen
import random


def main():
    my_turtle = Turtle()
    screen = Screen()
    my_turtle.shape("classic")
    # my_turtle.pensize(15)
    my_turtle.speed(0)
    screen.colormode(255)

    draw_spirograph(my_turtle, 150, 180)

    screen.exitonclick()


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_spirograph(turtle, size, numbers):
    angle = 360 / numbers
    for i in range(numbers):
        turtle.pencolor(random_color())
        turtle.circle(size)
        turtle.setheading(angle * (i+1))


def draw_random_walk(turtle, size, times):
    # colors = ["red", "blue", "green", "yellow",
    #           "brown", "orange", "aqua", "pink"]
    angles = [0, 90, 180, 270]
    for i in range(times):
        # turtle.color(random.choice(colors))
        turtle.pencolor(random_color())
        turtle.right(random.choice(angles))
        turtle.forward(size)


def draw_square(turtle, size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)


def draw_polygon(turtle, sides, size):
    angle = 360/sides
    for i in range(sides):
        turtle.forward(size)
        turtle.right(angle)


def draw_dash_line(turtle, size, a, b):
    times = int(round(size/(a+b), 0))
    for i in range(times):
        turtle.forward(a)
        turtle.penup()
        turtle.forward(b)
        turtle.pendown()


if __name__ == '__main__':
    main()
