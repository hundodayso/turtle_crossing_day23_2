import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Score

# from scoreboard import Scoreboard
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Score()
count = 0

screen.listen()
screen.onkeypress(fun=player.move_up, key="w")

game_is_on = True
car_manager.create_car()
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    # Add a new car every sixth loop
    if count == 6:
        count = 0
        car_manager.create_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            print("hello")

    if player.ycor() >= FINISH_LINE_Y:
        time.sleep(0.2)
        player.starting_position()
        scoreboard.show_score()
        car_manager.level_up()
        print("yoooo")



screen.exitonclick()

