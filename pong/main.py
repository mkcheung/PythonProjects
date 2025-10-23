from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_active = True
leftPaddleCoodinates = (-350,0)
rightPaddleCoodinates = (350,0)

leftPaddle = Paddle(leftPaddleCoodinates)
rightPaddle = Paddle(rightPaddleCoodinates)
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()
screen.onkey(leftPaddle.up, "w")
screen.onkey(leftPaddle.down, "s")
screen.onkey(rightPaddle.up, "Up")
screen.onkey(rightPaddle.down, "Down")



while game_active:
    screen.update() 
    time.sleep(0.1)
    ball.move()
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y()

    if((ball.distance(rightPaddle) < 50 and ball.xcor() > 340) or (ball.distance(leftPaddle) < 50 and ball.xcor() < -340)):
        ball.bounce_x()

    if(ball.xcor() < -400):
        scoreboard.leftIncrement();
        ball.reset()
    
    if(ball.xcor() > 400):
        scoreboard.rightIncrement();
        ball.reset()

screen.exitonclick()
