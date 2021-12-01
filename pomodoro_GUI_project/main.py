from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        timer_label.config(text="Working", fg=GREEN)
        count_down(round(WORK_MIN*60))
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(round(LONG_BREAK_MIN*60))
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(round(SHORT_BREAK_MIN*60))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_min_text = str(count_min) if count_min >= 10 else f"0{count_min}"
    count_sec = count % 60
    count_sec_text = str(count_sec) if count_sec >= 10 else f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min_text}:{count_sec_text}")
    global reps
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "🗸"
        check_mark.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro GUI")
window.config(padx=100, pady=50, bg=YELLOW)
timer_label = Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 24, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file="./pomodoro_GUI_project/tomato.png")
canvas.create_image(100, 113, image=tomato_img)
time_text = canvas.create_text(100, 128, text="00:00", fill="white",
                               font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
check_mark = Label(fg=GREEN, font=(FONT_NAME, 18, "bold"), bg=YELLOW)
check_mark.grid(column=1, row=3)
window.mainloop()
