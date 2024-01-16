import turtle
import colorgram
from turtle import Turtle, Screen
import random

colours = colorgram.extract("maxresdefault.jpg", 8)
# print(type(colours))
for index in range(len(colours)):
    colours[index] = tuple(colours[index].rgb)
# print(colours)

timmy = Turtle()
timmy.shape("arrow")
turtle.colormode(255)

timmy.setheading(225)
timmy.penup()
timmy.forward(250)
timmy.setheading(0)


def draw_a_line():
    for i in range(1, 11):
        the_color = random.choice(colours)
        timmy.dot(20, the_color)
        timmy.penup()
        if i != 10:
            timmy.fd(50)
    timmy.lt(90)
    timmy.fd(50)
    timmy.lt(90)
    timmy.fd(450)
    timmy.lt(180)


for _ in range(1, 11):
    draw_a_line()


screen = Screen()
screen.exitonclick()
