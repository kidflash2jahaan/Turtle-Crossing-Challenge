import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkeypress(player.moveup, "Up")
screen.onkeypress(player.movedown, "Down")
screen.onkeypress(player.moveleft, "Left")
screen.onkeypress(player.moveright, "Right")

game_is_on = True
loop_number = 0
while game_is_on:
    time.sleep(0.01)
    loop_number += 1
    scoreboard.level = player.level
    car_manager.level = player.level
    scoreboard.update()
    car_manager.move()
    if loop_number % (60 / player.level) == 0:
        car_manager.spawn()

    for car in car_manager.cars:
        if abs(car.xcor() - player.xcor()) <= 20 and abs(car.ycor() - player.ycor()) <= 20:
            scoreboard.stop()
    screen.update()
