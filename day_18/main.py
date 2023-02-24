from turtle import Turtle, Screen, colormode
from random import randint, choice


def random_colours():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(direction):
    colormode(255)
    tim.pencolor(random_colours())
    tim.pensize(3)
    tim.left(direction)
    tim.speed("fastest")
    tim.circle(100)


tim = Turtle()
tim.shape("turtle")
tim.color("blue")

for idx in range(0, 91):
    draw_shape(4)

screen = Screen()
screen.exitonclick()
