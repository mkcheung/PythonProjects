from turtle import Turtle, Screen, colormode
import random

rgbColors = [
    (245, 243, 238),
    (246, 242, 244),
    (202, 164, 110),
    (240, 245, 241),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
    (66, 64, 60),
    (219, 178, 183),
    (178, 198, 202),
    (112, 139, 141), 
    (254, 194, 0)
]

DISTANCE = 10
colormode(255)
t = Turtle()


def moveRight():
    if t.heading() != 0:
        t.color(random.choice(rgbColors))
        t.setheading(0)
    t.forward(DISTANCE)

def moveUp():
    if t.heading() != 90:
        t.color(random.choice(rgbColors))
        t.setheading(90)
    t.forward(DISTANCE)

def moveLeft():
    if t.heading() != 180:
        t.color(random.choice(rgbColors))
        t.setheading(180)
    t.forward(DISTANCE)

def moveDown():
    if t.heading != 270:
        t.color(random.choice(rgbColors))
        t.setheading(270)
    t.forward(DISTANCE)


screen = Screen()
screen.listen()
screen.onkey(moveUp, "Up")
screen.onkey(moveDown, "Down")
screen.onkey(moveRight, "Right")
screen.onkey(moveLeft, "Left")

screen.mainloop()

screen.exitonclick()