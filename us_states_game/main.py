from turtle import Turtle, Screen
import turtle
import pandas as pd


def write_state(name, x, y):
    tur = Turtle()
    tur.penup()
    tur.goto(x, y)
    tur.write(arg=name, font=("Times New Roman", 8, "normal"), align="center")
    tur.hideturtle()


def main():
    scr = Screen()
    scr.title("My U.S States Game")
    image = "blank_states_img.gif"
    turtle.register_shape(image)
    tur = Turtle(shape=image)
    data = pd.read_csv("50_states.csv")
    states = data.state.to_list()
    xcors = data.x.to_list()
    ycors = data.y.to_list()
    guessed_states = []
    game_is_on = True
    while game_is_on:
        guess = scr.textinput("Guess U.S States" if len(guessed_states) == 0 else f"Guessed {len(guessed_states)}/50 states",
                              "Whats's another state name?\nIf you want to stop the game, Click Cancel")
        if guess == None or guess.title() == "Exit":
            game_is_on = False
            missing_states = [
                state for state in states if state not in guessed_states]
            missing_data = pd.Series(missing_states)
            missing_data.to_csv("StatesToLearn.csv")
            break
        guess = guess.title()
        if guess in states:
            guessed_states.append(guess)
            i = states.index(guess)
            write_state(guess, xcors[i], ycors[i])

        if len(guessed_states) == 50:
            game_is_on = False


if __name__ == '__main__':
    main()
