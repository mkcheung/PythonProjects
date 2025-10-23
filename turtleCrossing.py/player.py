from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0, -280)
        self.color("black")
        self.setheading(90)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def right(self):
        self.goto(self.xcor() + 20, self.ycor())

    def onOtherSide(self):
        if self.ycor() >= 280:
            return True
        else:
            return False
    
    def reset(self):
        self.goto(0, -280)
        