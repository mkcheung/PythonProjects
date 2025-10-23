from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-280, 280)
        self.printLevel();

    def printLevel(self):
        self.level += 1
        self.clear()
        self.goto(-240, 280)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))
                   
    def printGameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Courier", 20, "normal"))
                
