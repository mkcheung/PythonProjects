import random
from turtle import Turtle

colors = ["red", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        initial = -300
        self.racingCars = []
    
    def createCar(self):
        t = Turtle(shape='square')
        t.penup()
        t.color(random.choice(colors))
        t.shapesize(stretch_wid=1, stretch_len=2)
        t.setheading(180)
        randomY = random.randint(-250, 250)
        t.goto(300, randomY)
        self.racingCars.append(t)

    def move(self):
        for racingCarIndex in range(len(self.racingCars)): 
            distance = random.randint(2, 7)
            self.racingCars[racingCarIndex].forward(distance)


