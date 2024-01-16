from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.goto(x, y)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def up(self):
        self.penup()
        self.setpos(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def down(self):
        self.penup()
        self.setpos(self.xcor(), self.ycor()-MOVE_DISTANCE)
