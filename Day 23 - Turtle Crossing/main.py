import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.bgcolor("black")
screen.title("Reenie the turtle")
screen.setup(width=600, height= 600)
screen.tracer(0)

reenie = Player()
gorgor = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(reenie.go_up, "Up")

loop = 0
is_hit = False
level = 1
while not is_hit:
    time.sleep(0.1)
    screen.update()
    #my solution using loop and modulus, not proper because will create less car after speed increase
    if loop % (7 - level) == 0:
    #angela solution
    #if randint(1, 7 - level) == 1:
        gorgor.add_car()
    gorgor.move()
    loop += 1

    is_hit = gorgor.check_distance(reenie)

    if is_hit:
        scoreboard.game_over()
        break
    is_reach_goal = reenie.check_goal()
    if is_reach_goal:
        reenie.restart()
        level += 1
        scoreboard.update_level(level)
        #scoreboard.add_level()
        gorgor.increase_speed()

screen.exitonclick()