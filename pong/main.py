from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

game_active = True
leftPaddleCoodinates = (-350,0)
rightPaddleCoodinates = (350,0)

leftPaddle = Paddle(leftPaddleCoodinates)
rightPaddle = Paddle(rightPaddleCoodinates)
ball = Ball()

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
        ball.bounce()


screen.exitonclick()
