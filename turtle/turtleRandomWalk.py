from turtle import Turtle, Screen, colormode
import random

colormode(255)
t = Turtle()
# colors = ["red", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
headings = [90, 180, 270, 360]
distance = 100
penSizes = [40, 52, 23, 10]

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for i in range(1, 20):
    # t.color(random.choice(colors))
    t.pensize(random.choice(penSizes))
    t.color(randomColor())
    t.forward(distance)
    t.setheading(random.choice(headings))

screen = Screen()
screen.exitonclick()