from turtle import Turtle, Screen, colormode
import random;

t = Turtle()
colormode(255)
t.speed("fastest")

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range(100):
    t.color(randomColor())
    t.circle(100)
    t.setheading(t.heading()+10)

screen = Screen()
screen.exitonclick()