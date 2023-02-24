import turtle
from turtle import Turtle, Screen, colormode
from random import choice


# import colorgram
#
#
# colors = colorgram.extract("Anime-girl.jpeg", 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

def draw_dot():
    colormode(255)
    tim.speed("fastest")
    tim.dot(20, choice(color_list))
    tim.forward(50)


def new_line():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)


size = 10
tim = Turtle()
tim.penup()
tim.hideturtle()

color_list = [(250, 206, 241), (253, 234, 218), (243, 58, 118), (249, 152, 205), (244, 114, 165), (179, 6, 55), (53, 179, 244), (177, 252, 249), (1, 175, 251), (103, 252, 247), (202, 226, 250), (209, 29, 85), (232, 131, 109), (76, 235, 249), (109, 3, 16), (23, 17, 16), (252, 167, 144), (172, 177, 245), (6, 24, 56), (116, 91, 81), (51, 103, 154), (85, 120, 201), (213, 94, 70), (19, 22, 20), (12, 58, 152), (90, 95, 94), (120, 38, 26), (156, 161, 159), (234, 196, 137), (170, 124, 79)]

tim.setheading(220)
tim.forward(300)
tim.setheading(0)

for y in range(size):
    for x in range(size):
        draw_dot()
    new_line()


screen = Screen()
screen.exitonclick()
