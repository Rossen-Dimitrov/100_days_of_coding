from turtle import Turtle


class CorrectAnswer(Turtle):
    def __init__(self, x, y, state_name):
        super().__init__()
        self.state_name = state_name
        self.x = x
        self.y = y
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(self.state_name, align="center", font=("Courier", 8, "normal"))
