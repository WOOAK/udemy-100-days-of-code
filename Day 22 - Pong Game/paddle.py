from turtle import Turtle
class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        ypos = self.ycor()
        self.goto(self.xcor(), ypos + 20)

    def go_down(self):
        ypos = self.ycor()
        self.goto(self.xcor(), ypos - 20)