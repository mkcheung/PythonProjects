from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0,260)
        self.hideturtle()

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "bold"))