from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_is_on = False

turtles = []

y = -85
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-240, y=y)
    y += 35
    turtles.append(turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() > 210:
            break

screen.exitonclick()
