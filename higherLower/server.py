from flask import Flask
from game_data import data
import random

app = Flask(__name__)
randomNumber = 0;


def selectRandom(function):
    def pickRandom():
        global randomNumber
        randomNumber = random.randint(0,9)
        print(randomNumber)
        return function()
    return pickRandom

@app.route("/")
@selectRandom
def guessNumber():
    return (
        '<h1 style="text-align: center;">Guess a number between 0 and 9</h1>'
        '<img style="display: block; margin: auto;" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'
    )

@app.route("/URL/<int:guessedNum>")
def checkNumber(guessedNum):
    if guessedNum < randomNumber:
        return (
            '<h1 style="text-align: center; color: red">Too low, try again!</h1>'
            '<img style="display: block; margin: auto;" src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExemVwbWR2d2V1aXJpaTBreGlmdWNzY3ByaDMxY252eXh2ZnVsazh0biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2JhueyxhPxP8WtPy/giphy.gif" />'
        )
    elif guessedNum > randomNumber:
        return (
            '<h1 style="text-align: center; color: blue">Too high, try again!</h1>'
            '<img style="display: block; margin: auto;" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDg5aGlkNW5qbWEwcjRhMDQ1ZXVmZHkyaWp0YzlzcHRtZjk3YXd2aiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/H9bn1yn9ScQ6s/giphy.gif" />'
        )
    else:
        return (
            '<h1 style="text-align: center; color: blue">Correct!</h1>'
            '<img style="display: block; margin: auto;" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmlxN3k4NTd6ZmpybnhmbmprcTdub284OTVxazJmbDJqeDR1ZHVzNCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/wofyg8nxsWEmtR7eOK/giphy.gif" />'
        )