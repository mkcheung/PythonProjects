from food import Food
from snakeModel import Snake
import time
from turtle import Screen


game_active = True
startingLocations = [(0,0), (-20,0), (-40,0), (-60,0)]

snake = Snake(startingLocations)
food = Food()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

while game_active:
    screen.update() 
    time.sleep(0.1)
    snake.move()
    if snake.head().distance(food) < 15:
        food.refresh()

screen.exitonclick()