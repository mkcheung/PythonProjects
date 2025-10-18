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

# Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word.
# At that point `display` has no more blanks ("_"). Then you can tell the user they've won.

# Create a variable called `lives` to keep track of the number of lives left.
# Set `lives` to equal `6`.

# If `guess` is not a letter in the `chosen_word`, Then reduce `lives` by `1`. 
# If `lives` goes down to `0` then the game should end, and it should print "You lose."

# print the ASCII art from the list `stages` that corresponds to the current number of `lives` the user has remaining.
import random
import hangman_words

placeholder = ''
game_over = False
lives = 6


chosen_word = random.choice(hangman_words.word_list).lower()

numChars = len(chosen_word)
for i in range(0, numChars):
    placeholder += "_"

print(placeholder)

correctLetters = []
guessedLetters = []

while not game_over:

    print(f"************************ {lives} Remaining ************************")

    guess = input(f"Please guess a letter.\n").lower()
    display = ''

    if guess in guessedLetters:
        print(f"{guess} is already one of the letters you had guessed previously.")
        continue

    for char in chosen_word:
        if(char == guess):
            display += char
            correctLetters.append(char)
        elif(char in correctLetters):
            display += char
        else:
            display += '_'

    print(display)

    if(guess not in chosen_word):
        print(f"'{guess}' is not in the chosen word.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if( '_' not in display):
        game_over = True
        print("You win.")
        
    guessedLetters.append(guess)