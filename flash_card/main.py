from tkinter import *
import pandas as pd
import random
import time
import os
BACKGROUND_COLOR = "#B1DDC6"
french_words_filepath = "./flash_card/data/french_words.csv"
words_to_learn_filepath = "./flash_card/data/words_to_learn.csv"
filepath = words_to_learn_filepath if os.path.exists(
    words_to_learn_filepath) else french_words_filepath
data = pd.read_csv(
    filepath).to_dict(orient="records")
current_card = {}
# ---------------------------- GEN RANDOM WORD ------------------------------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def know_word():
    data.remove(current_card)
    data_frame = pd.DataFrame(data)
    data_frame.to_csv("./flash_card/data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="./flash_card/images/card_front.png")
card_back_image = PhotoImage(file="./flash_card/images/card_back.png")
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(
    400, 150, font=("Arial", 40, "italic"), text="French")
word_text = canvas.create_text(
    400, 293, font=("Arial", 60, "bold"), text="trouve")
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./flash_card/images/right.png")
wrong_image = PhotoImage(file="./flash_card/images/wrong.png")
right_btn = Button(image=right_image, highlightthickness=0,
                   borderwidth=0, command=know_word)
right_btn.grid(row=1, column=1)
wrong_btn = Button(image=wrong_image, highlightthickness=0,
                   borderwidth=0, command=next_card)
wrong_btn.grid(row=1, column=0)
flip_timer = window.after(3000, flip_card)
next_card()
window.mainloop()
