from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()
tim.shape("turtle")
tim.color("green4")

# draw a square with 100
# tim.fd(100)
# tim.lt(90)
# tim.fd(100)
# tim.lt(90)
# tim.fd(100)
# tim.lt(90)
# tim.forward(100)

# draw a discontinued line, 15 times
# for _ in range(15):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()


# draw different shapes with different number of sides
# colours = ["green1", "IndianRed1", "blue1", "cyan2", "magenta", "navy", "purple", "tomato"]
tim.shape("arrow")
#
#
# def draw_shape(num_sides):
#     corner_degree = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.rt(corner_degree)
#
#
# for item in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(item)


# set a random colour from RGB collection
turtle.colormode(255)
# tim.pensize(6)
# directions = [0, 90, 180, 270]
tim.speed("fastest")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour
#
# for _ in range(100):
#     tim.color(random_colour())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    for item in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
screen = Screen()
screen.exitonclick()
