# Create an empty String called `placeholder`.
# For each letter in the chosen_word, add a `_` to `placeholder`.
# So if the `chosen_word` was "apple", `placeholder` should be `_ _ _ _ _` with 5 `"_"` representing each letter to guess.
# Print out `hint`.

# Create an empty string called "display".
# Loop through each letter in the `chosen_word`
# If the letter at that position matches `guess` then reveal that letter in the `display` at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then `display` should be `_ p p _ _`.
# Print `display` and you should see the guessed letter in the correct position.
# But every letter that is not a match is represented with a "_".
import random

placeholder = ''

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list).lower()

numChars = len(chosen_word)
for i in range(0, numChars):
    placeholder += "_"

print(placeholder)

display = ''

guess = input(f"Please guess a letter.\n")

for char in chosen_word:
    if(char == guess):
        display += char
    else:
        display += '_'

print(display)