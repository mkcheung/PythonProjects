from turtle import Turtle, Screen

t = Turtle()

t.color("red")
# pentagon
for i in range (1,6):
    t.forward(100)
    t.right(72)

#square
for i in range (1,5):
    t.forward(100)
    t.right(90)

#triangle
for i in range (1,4):
    t.forward(100)
    t.right(120)

#triangle
for i in range (1,7):
    t.forward(100)
    t.right(60)

screen = Screen()
screen.exitonclick()