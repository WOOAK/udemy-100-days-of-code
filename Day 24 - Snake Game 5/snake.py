from turtle import Turtle
import time
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        xx = 0
        yy = 0X
        for count in range(3):
            self.add_segment(xx, yy)
            xx -= MOVE_DISTANCE
    def add_segment(self, xx, yy):
        snake = Turtle()
        snake.color("white")
        snake.penup()
        snake.goto(xx, yy)
        snake.shape("square")
        self.segments.append(snake)

    def extend(self):
        xx = self.segments[-1].xcor()
        yy = self.segments[-1].ycor()
        self.add_segment(xx, yy)

    def reset(self):
        for seg in range(len(self.segments)):
            self.segments[seg].goto(0, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            old_xpos = self.segments[seg - 1].xcor()
            old_ypos = self.segments[seg - 1].ycor()
            self.segments[seg].goto(old_xpos, old_ypos)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)




