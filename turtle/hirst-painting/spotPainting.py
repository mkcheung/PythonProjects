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

colormode(255)
t = Turtle()
t.speed('fastest')

def drawDottedGrid(numRows, numPositions, distance):
    for i in range(numRows):
        for j in range(numPositions):
            t.pendown()
            randomColor = random.choice(rgbColors)
            t.color(randomColor)
            t.dot();
            t.penup()
            if j != numPositions-1:
                t.forward(distance)
        if i % 2 == 0:
            t.right(90)
            t.forward(distance)
            t.right(90)
        else:
            t.left(90)
            t.forward(distance)
            t.left(90)

drawDottedGrid(10, 10, 50)

screen = Screen()
screen.exitonclick()