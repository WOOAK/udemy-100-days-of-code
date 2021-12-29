from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_objects = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.count = 0

    def add_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        random_color = random.choice(COLORS)
        new_car.color(random_color)
        random_ypos = random.choice(range(-250, 251))
        new_car.goto(280, random_ypos)
        new_car.setheading(180)
        self.car_objects.append(new_car)

    def move(self):
        for step in range(0, len(self.car_objects)):
            self.car_objects[step].forward(self.move_distance)

    def check_distance(self, bella):
        is_hit = False
        for steps in range(len(self.car_objects)):
            # print(self.car_objects[steps].ycor())
            # print(bella.ycor())
            # print(self.car_objects[steps].xcor())
            # print(bella.xcor())
            #
            # print(steps)
            #if abs(bella.ycor() - self.car_objects[steps].ycor()) <= 25 and abs(bella.xcor() - self.car_objects[steps].xcor()) <= 15:
            if bella.distance(self.car_objects[steps]) <= 20:
                is_hit = True
                break
        return is_hit

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT








