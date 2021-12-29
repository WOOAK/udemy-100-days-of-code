from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, "italic")

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()


    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)