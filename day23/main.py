# Turtle Crossing Project

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:  # checking for collision with moving cars, if yes, restart game!
            player.reset_position()
            scoreboard.reset_score()

    if player.ycor() > 280:  # checking if player reached finish point and increasing level and increasing car speed
        player.reset_position()
        scoreboard.level_track()
        car_manager.increase_speed()

screen.exitonclick()
