from turtle import Turtle, Screen
import random

t = Turtle()
colors = ["red", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
headings = (90, 180, 270, 360)
distance = 100

for i in range(1, 20):
    t.color(random.choice(colors))
    t.forward(distance)
    t.setheading(random.choice(headings))

screen = Screen()
screen.exitonclick()