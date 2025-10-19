import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculateSum(cards):
    total = sum(cards)
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

playerDealtCards = []
computerDealt = []
computerTotal = 0
activeHits = True;

for num in range(0, 2):
    playerDealtCards.append(deal_card())
    computerDealt.append(deal_card())

print(f"You have cards {playerDealtCards[0]} {playerDealtCards[1]}")
print(f"Computer shows one card: {computerDealt[0]}")

while activeHits:
    playerTotal = 0
    newCard = input("Hit? Please enter 'y' or 'n': ")
    playerCardsAndTotal = ''

    if newCard == 'y':
        cards = ''
        playerDealtCards.append(deal_card())
        for num in playerDealtCards:
            cards +=  f"{num}, "

    playerTotal = calculateSum(playerDealtCards)  

    print(f"Player cards: {cards} - Total: {playerTotal}")

    if playerTotal > 21 or newCard == 'n':
        activeHits = False
    
    computerTotal = calculateSum(computerDealt)  

if playerTotal > 21 or computerTotal <= 21 and playerTotal < computerTotal:
    print(f"Player {playerTotal} : Computer {computerTotal} - You Lose!")
elif playerTotal > computerTotal:
    print(f"Player {playerTotal} : Computer {computerTotal} - You Win!")
elif playerTotal == computerTotal:
    print(f"Player {playerTotal} : Computer {computerTotal} - Draw")





