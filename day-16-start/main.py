from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["electric", "water", "fire"])
print(table)
table.align = "l"
