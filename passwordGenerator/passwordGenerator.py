import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Password Generator')

numberOfLetters = int(input("Please enter in the number of letters you want in your password:\n"))
numberOfNumbers = int(input(f"Please enter in the number of digital numbers you want in your password:\n"))
numberOfSymbols = int(input(f"Please enter in the number of symbols you want in your password:\n"))

totalPWlength = numberOfLetters + numberOfNumbers + numberOfSymbols
password = ''
while(len(password) < totalPWlength):
    randomNumber = random.randint(1,3)
    if(randomNumber == 1 and numberOfLetters > 0):
        randLetter = random.choice(letters)
        password = password + randLetter
        numberOfLetters-=1
    if(randomNumber == 2 and numberOfNumbers > 0):
        randNumber = random.choice(numbers)
        password = password + str(randNumber)
        numberOfNumbers-=1
    if(randomNumber == 3 and numberOfSymbols > 0):
        randSymbol = random.choice(symbols)
        password = password + randSymbol
        numberOfSymbols-=1

print(password)