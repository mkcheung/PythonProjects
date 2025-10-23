from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color('white')
        self.speed("fastest")
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10

    def reset(self):
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        newX = self.xcor() + self.x_move
        newY = self.ycor() + self.y_move
        self.goto(newX, newY)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
