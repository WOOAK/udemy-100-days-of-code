from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(600, 600)
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
    time.sleep(0.3)
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    snake.move()
    #eat food
    if snake.head.distance(food) <= 15:
        food.create_food()
        score.add_score()
        snake.extend()
    #bang wall
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        #game_is_on = False
        #score.game_over()
        score.reset()
        snake.reset()
    #hit sendiri
    #for segment in snake.segments:
    #slicing
    for segment in snake.segments[1:]:
        #if segment == snake.head:
        #    pass
        #elif snake.head.distance(segment) < 10:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #score.game_over()
            score.reset()
            snake.reset()
screen.exitonclick()
