from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "italic")

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

