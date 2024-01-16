import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(6)

timmy = Player()
manager = CarManager()
last_spawn = 0
level = 1
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=timmy.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard(level)

    if last_spawn + 1 < time.time():
        manager.create_car()
        last_spawn = time.time()
    manager.move()

    # Detect collision with car
    for car in manager.all_cars:
        if timmy.distance(car) < 20:
            timmy.goto(0, 0)
            timmy.write("Game over", align="center", font=("Courier", 50, "normal"))
            game_is_on = False

    # Detect successful crossing
    if timmy.is_at_finish_line():
        timmy.go_to_start()
        manager.level_up()
        level += 1

screen.exitonclick()
