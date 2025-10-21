from turtle import Screen
import time
from snakeModel import Snake

game_active = True
startingLocations = [(0,0), (-20,0), (-40,0), (-60,0)]
snake = Snake(startingLocations)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

while game_active:
    screen.update() 
    time.sleep(0.1)
    snake.move()

screen.exitonclick()