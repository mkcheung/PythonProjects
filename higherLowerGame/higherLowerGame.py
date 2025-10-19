from art import logo
from art import vs
from game_data import data
import random

score = 0
comparables = random.sample(data, 2)
continueGame = True

while continueGame:

    print(data)
    print(comparables)
    print(logo)

    print(f"Compare A: {comparables[0]['name']}, a {comparables[0]['description']}, from {comparables[0]['country']}.")

    print(vs)

    print(f"Against B: {comparables[1]['name']}, a {comparables[1]['description']}, from {comparables[1]['country']}.")

    guessOfBestFollowers = input("Who has more followers? Type 'A' or 'B': ")

    if((guessOfBestFollowers == 'A' and comparables[0]['follower_count'] > comparables[1]['follower_count']) or (guessOfBestFollowers == 'B' and comparables[1]['follower_count'] > comparables[0]['follower_count'])):
        score += 1
        print("\n" * 20)
        comparables = random.sample(data, 2)
    elif((guessOfBestFollowers == 'A' and comparables[0]['follower_count'] < comparables[1]['follower_count']) or (guessOfBestFollowers == 'B' and comparables[1]['follower_count'] < comparables[0]['follower_count'])):
        print(logo) 
        print(f"Sorry , that's wrong. Final score: {score}") 
        continueGame = False
    else:
        print("exit");
