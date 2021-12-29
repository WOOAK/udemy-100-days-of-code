# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# print(colors)
# rgb_colors = []
# for colour in colors:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
# extract colours and put to color_list
import random
import turtle as t
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
 (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
 (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
 (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t.colormode(255)
tim = t.Turtle()


def start_at_left(size):
    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.left(90)
    tim.forward((size-1)*50)
    tim.left(180)


def starting():
    tim.setheading(225)
    tim.penup()
    tim.speed("fastest")
    tim.hideturtle()
    tim.forward(225)
    tim.setheading(0)
    #tim.pendown()


def draw_hirst(size):

    starting()
    for row in range(size):
        for column in range(size):
            colour = random.choice(color_list)
            tim.dot(20, colour)
            #tim.penup()
            if column != (size-1):
                tim.forward(50)
            #tim.pendown()
        if row != (size-1):
            start_at_left(size)


draw_hirst(10)



screen = t.Screen()
screen.exitonclick()
