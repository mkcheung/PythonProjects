
import os
from turtle import Turtle, Screen
from pathlib import Path
import pandas

guessedStates = []
screen = Screen()
screen.title("U.S. States Game")
workingDirectory = Path(__file__).resolve().parent 
image = f"{workingDirectory}/blank_states_img.gif"
screen.addshape(image)
toScreen = Turtle()
toScreen.shape(image)

t = Turtle()
t.penup()
t.color('black')
t.speed('fastest')
t.hideturtle()

data = pandas.read_csv(f"{workingDirectory}/50_states.csv");
stateList = data.state.to_list();
while len(guessedStates) < 50:
    answer_state = screen.textinput(title="Guess The State", prompt="What's another states's name?").title()
    guessedStates.append(answer_state)

    if answer_state == 'Exit':
        missing_states = [ state for state in stateList if state not in guessedStates ]
        outputDF = pandas.DataFrame(missing_states)
        outputDF.to_csv("statesToLearn.csv")
        break

    if answer_state in stateList:
        stateDF = data[data.state == answer_state]
        t.goto(stateDF.x.item(),stateDF.y.item())
        t.write(f"{answer_state}")