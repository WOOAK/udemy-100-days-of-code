from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=350, height=500, padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300,height=250)
        self.score = Label(text = "Score = 0",bg=THEME_COLOR)
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, command=self.check_true)
        self.wrong_button = Button(image=self.false_image, command=self.check_wrong)

        self.canvas.grid(row=1, column=0,columnspan=2, pady= 50)
        self.true_button.grid(row=2, column=0, sticky="W")
        self.wrong_button.grid(row=2, column=1, sticky="E")
        self.score.grid(row=0, column=1)
        # self.canvas.create_text(150, 125, text="Any question",font = ("Arial", 20, "italic"))
        self.question_text = self.canvas.create_text(
            150, 125, text="Any question",
            font = ("Arial", 20, "italic"),
            width=300)
        if self.quiz.still_has_questions():
            self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def give_feedback(self, true_ind):
        if true_ind:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

    def next_action(self):
        if self.quiz.still_has_questions():
            self.enable_buttons()
            self.get_next_question()
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text = "You have completed the quiz!")
            self.disable_buttons()



    def check_true(self):
        score, total, is_correct = self.quiz.check_answer("True")
        self.score.config(text=f"Score: {score}/{total}")
        self.give_feedback(is_correct)
        self.disable_buttons()
        self.window.after(1000, self.next_action)

    def check_wrong(self):
        score, total, is_correct = self.quiz.check_answer("False")
        self.score.config(text=f"Score: {score}/{total}")
        self.give_feedback(is_correct)
        self.disable_buttons()
        self.window.after(1000, self.next_action)

    def enable_buttons(self):
        self.true_button["state"] = "active"
        self.wrong_button["state"] = "active"

    def disable_buttons(self):
        self.true_button["state"] = "disabled"
        self.wrong_button["state"] = "disabled"