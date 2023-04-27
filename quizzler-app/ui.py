from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
import time


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=30)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial",14))
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     width=290,
                                                     font=("Arial",20,"italic"))

        self.true_image = PhotoImage(file="images/true.png", width=100, height=97)
        self.false_image = PhotoImage(file="images/false.png", width=100, height=97)

        self.false_btn = Button(image=self.false_image, highlightthickness=0, command=self.false_button_clicked)
        self.false_btn.grid(row=2, column=0)

        self.true_btn = Button(image=self.true_image, highlightthickness=0, command=self.true_button_clicked)
        self.true_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.configure(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            if not self.quiz.still_has_questions():
                self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
                self.canvas.configure(bg="white")
                self.true_btn.configure(state=DISABLED)
                self.false_btn.configure(state=DISABLED)
    def true_button_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
