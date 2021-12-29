from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(600, 600)
#screen.bgpic("snake-game.gif")
screen.bgcolor("black")
screen.title("'Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

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
    if snake.head.distance(food) <= 15:
        food.create_food()
        score.add_score()
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        game_is_on = False
        score.game_over()
screen.exitonclick()
