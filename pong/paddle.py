from turtle import Turtle
DISTANCE = 20
DOWN = 90
UP = 270

class Paddle(Turtle):
    def __init__(self, startingLocation):
        super().__init__()
        self.penup()
        self.goto(startingLocation)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)