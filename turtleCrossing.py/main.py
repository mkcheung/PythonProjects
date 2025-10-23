import time
from cars import Cars
from turtle import Screen
from player import Player
from scoreboard import Scoreboard


gameActive = True;
player = Player()
scoreboard = Scoreboard()
screen = Screen()
screen.tracer(0)
screen.listen()
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.setup(600, 600)
cars = Cars()
screen.bgcolor("white")

while gameActive:
    time.sleep(0.1)
    cars.createCar()
    cars.move()
    screen.update()
    for car in cars.racingCars:
        if car.distance(player) < 20:
            scoreboard.printGameOver()
            gameActive = False
    if player.onOtherSide():
        scoreboard.printLevel()
        player.reset()

screen.exitonclick()