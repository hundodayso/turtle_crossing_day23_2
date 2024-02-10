from turtle import Turtle
import random

START_X_POS = 300
CAR_COLOURS = ["red", "blue", "yellow", "green", "orange", "purple", "magenta"]
CAR_MOVE_DISTANCE = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = CAR_MOVE_DISTANCE


    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.color(random.choice(CAR_COLOURS))
        new_car.setpos(START_X_POS, random.randint(-250, 250))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car_new_xpos = car.xcor() - self.car_speed
            car.setx(car_new_xpos)
            print(self.car_speed)

    def level_up(self):
        self.car_speed *= 1.5
