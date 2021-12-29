from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(600, 600)
#screen.bgpic("snake-game.gif")
screen.bgcolor("black")
screen.title("'Snake Game")
screen.tracer(0)

snake = Snake()

    #snake.forward(90)
game_is_on = True
screen.listen()

while game_is_on:
    screen.update()
    time.sleep(0.5)
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    snake.move()



screen.exitonclick()
