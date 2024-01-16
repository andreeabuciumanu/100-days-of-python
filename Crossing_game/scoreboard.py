
from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self, level):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level:{level}", align="center", font=FONT)

