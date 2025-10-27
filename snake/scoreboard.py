import os
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        if os.path.exists("./high_score.txt"):
            with open("./high_score.txt", "r") as file:
                self.high_score = int(file.read());
        else:
            self.high_score = 0
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./high_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increment(self):
        self.score += 1
        self.update_scoreboard()
