from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('green')
        self.speed("fastest")
        self.create_food()

    def create_food(self):
        xpos = randint(-280, 280)
        ypos = randint(-280, 280)
        self.goto(xpos, ypos)



