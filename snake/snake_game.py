from food import Food
from snakeModel import Snake
from scoreboard import Scoreboard
import time
from turtle import Screen



game_active = True
startingLocations = [(0,0), (-20,0), (-40,0), (-60,0)]

snake = Snake(startingLocations)
food = Food()
theScoreBoard = Scoreboard();

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
        snake.extend()
        theScoreBoard.increment()
    
    if snake.head().xcor() > 280 or snake.head().xcor() < -280 or snake.head().ycor() > 280 or snake.head().ycor() < -280:
        game_active = False
        print("Snake hit the wall! Game over.")

    for turtleSegment in snake.turtleSegments:
        if turtleSegment == snake.head():
            pass
        elif snake.head().distance(turtleSegment) < 10:
            game_active = False
            print("Snake hit it's own tail! Game over.")
            
screen.exitonclick()