from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzle")

        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_label = Label(text="Score : 0", fg="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=270, text="Amazon", font=("Arial", 20, "italic"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

