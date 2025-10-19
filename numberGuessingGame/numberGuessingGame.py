import art
import random

def checkNumber(target, selection):
    if selection < target:
        print(f"Target is greater than {selection}")
    else:
        print(f"Target is less than {selection}")
    return int(input("Please enter the next guess: "))
    
print(art.logo)

targetNumber = random.randint(1,100)
tries = 0

difficulty = input("Enter the difficulty level: ")

if difficulty == 'hard':
    tries = 3
elif difficulty == 'medium':
    tries = 5
else:
    tries = 10

guess = int(input("Please enter a guess: "))
while tries > 0 and guess != targetNumber:
    print(f"{guess} {targetNumber}")
    guess = checkNumber(target=targetNumber, selection=guess)
    tries -= 1

if guess == targetNumber:
    print(f"You guessed {guess}. Target was {targetNumber}. Nice Guess!")
else:
    print("No more guesses. Sorry!")