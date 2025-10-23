from turtle import Turtle;

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.leftScore = 0
        self.rightScore = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(-100, 200)
        self.displayLeft()
        self.goto(100, 200)
        self.displayRight()

    def displayLeft(self):
        self.write(f"{self.leftScore}", align="center", font=("Courier", 80, "normal"))

    def displayRight(self):
        self.write(f"{self.rightScore}", align="center", font=("Courier", 80, "normal"))

    def display(self):
        self.goto(-100, 200)
        self.displayLeft()
        self.goto(100, 200)
        self.displayRight()


    def leftIncrement(self):
        self.leftScore += 1
        self.clear()
        self.display()

    def rightIncrement(self):
        self.rightScore += 1
        self.clear()
        self.display()
