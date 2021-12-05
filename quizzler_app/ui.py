from tkinter import *

from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUI():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("My Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, font=(
            "Arial", 20, "italic"), text="Question here", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        true_img = PhotoImage(file=".\quizzler_app\images\\true.png")
        false_img = PhotoImage(file=".\quizzler_app\images\\false.png")
        self.true_btn = Button(
            image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(
            image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_btn.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(
                self.question_text, text=f"You've reached 10 question. Your score is {self.quiz.score}/10")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.canvas.config(bg="green" if is_right else "red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1500, self.get_next_question)
