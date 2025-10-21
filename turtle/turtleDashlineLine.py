from turtle import Turtle, Screen

t = Turtle()

t.color("red")
for i in range(1, 10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

screen = Screen()
screen.exitonclick();