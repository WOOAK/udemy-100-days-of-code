from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(600, 600)
#screen.bgpic("snake-game.gif")
screen.bgcolor("black")
screen.title("'Snake Game")
screen.tracer(0)
segments = []
xx = 0
yy = 0

for count in range(3):
    snake = Turtle()
    snake.color("white")
    snake.penup()
    snake.goto(xx, yy)
    snake.shape("square")
    xx -= 20
    segments.append(snake)
    #snake.forward(90)
game_is_on = True

print(len(segments))
while game_is_on:
    screen.update()
    time.sleep(0.5)


    #for seg in segments:
    #    seg.forward(20)
    for seg in range(len(segments)-1, 0, -1):

        #if seg != 0:
        old_xpos = segments[seg - 1].xcor()
        old_ypos = segments[seg - 1].ycor()
        segments[seg].goto(old_xpos, old_ypos)
        #else:
        #segments[seg].forward(20)
    segments[0].forward(20)

screen.exitonclick()
