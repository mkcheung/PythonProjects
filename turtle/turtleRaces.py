from turtle import Turtle, Screen
import random

racingTurtles = []
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
initialPosition = -100
raceActive = False

screen = Screen()
screen.setup(width=500, height=400)

for color in colors:
    t = Turtle(shape="turtle")
    t.penup()
    t.color(color)
    t.goto(-230, initialPosition)
    initialPosition += 50
    racingTurtles.append(t)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Please enter a color: ")
if user_bet:
    raceActive = True

while raceActive:
    randomDistance = random.randint(0,10)
    randomTurtle = random.choice(racingTurtles)
    randomTurtle.forward(randomDistance)

    for turtle in racingTurtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if(winner == user_bet):
                print(f"You've won! {winner} is the winning turtle!")
            else:
                print(f"You've lost. {winner} is the winning turtle.")
            raceActive = False
    

screen.exitonclick()