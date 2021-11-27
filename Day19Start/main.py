
from turtle import Turtle, Screen
import random
scr = Screen()
scr.setup(500, 400)
colors = ["red", "green", "blue", "black", "orange", "pink"]
lst_tur = []
for i in range(len(colors)):
    item = Turtle(shape="turtle")
    item.color(colors[i])
    item.penup()
    item.goto(-240, -150+i*50)
    lst_tur.append(item)
user_bet = scr.textinput("Choose the turtle",
                         f'Choose the turtle who will win the race ({"/".join(colors)}): ')
is_race_on = False
winner = None
if user_bet:
    is_race_on = True
while is_race_on:
    for i in range(len(lst_tur)):
        lst_tur[i].forward(random.randint(2, 10))
        if lst_tur[i].xcor() >= 250:
            winner = i
            is_race_on = False
            break
lst_tur[winner].goto(0, 0)
for i in range(len(lst_tur)):
    if i != winner:
        lst_tur[i].hideturtle()
winning_color = lst_tur[winner].pencolor()
if winning_color == user_bet:
    print(f"You've won. The {winning_color} turtle is the winner")
else:
    print(f"You've lost. The {winning_color} turtle is the winner")

# def move_forward():
#     tur.forward(50)


# def move_backward():
#     tur.backward(50)


# def turn_left():
#     tur.left(90)


# def turn_right():
#     tur.right(90)


# def clear_turtle():
#     tur.setposition(0, 0)
#     tur.clear()


# scr.listen()
# scr.onkey(turn_left, "a")
# scr.onkey(turn_right, "d")
# scr.onkey(move_forward, "w")
# scr.onkey(move_backward, "s")
# scr.onkey(clear_turtle, "c")
scr.exitonclick()
