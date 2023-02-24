from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
        self.goto(-100, 200)

    def update_scoreboard(self):
        self.clear()
        self.write(self.score, align="center", font=("Courier", 80, "normal"))
