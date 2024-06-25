from random import randint, choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 0

    def spawn(self):
        car = Turtle()
        car.speed(0)
        car.shape("square")
        car.shapesize(1, 2)
        car.color(choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(300, randint(-250, 250))

        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward((STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.level)) / 10)
