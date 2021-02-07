import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(fun=player.move_up, key="w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Create cars
    carmanager.create_cars()
    carmanager.move_cars()

    for car in carmanager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect if the turtle player has reached the top edge of the screen.
    if player.reached_finish_line():
        player.reset_position()
        carmanager.increment_speed()
        scoreboard.increment_point()






screen.exitonclick()