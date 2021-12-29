from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



# def move_forwards():
#     tim.forward(10)
#
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clockwise_curve():
    for i in range(10):
        tim.right(1)
        tim.forward(1)


def anticlockwise_curve():
    for i in range(10):
        tim.left(1)
        tim.forward(1)


def anticlockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def cleardraw():
    tim.reset()


screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=anticlockwise)
screen.onkey(key="Right", fun=clockwise)
#screen.onkey(key="m", fun=clockwise_curve)
#screen.onkey(key="n", fun=anticlockwise_curve)
screen.onkey(key="c", fun=cleardraw)

screen.exitonclick()
