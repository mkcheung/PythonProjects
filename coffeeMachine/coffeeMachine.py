from resourcesAndMenu import MENU
from resourcesAndMenu import resources

resources['Money'] = 0
options = ["espresso", "latte", "cappucino"]
coffeeMachineActive = True
profit = 0;

def checkResources(ingredients):
    for key in ingredients:
        if ingredients[key] < resources[key]:
            print(f"Not enough {key}")
            return False
    return True

def displayResources():
    itemsInMilliliters = ['water', 'milk']
    itemsInGrams = ['coffee']
    for key in resources:
        if key in itemsInMilliliters:
            print(f"{key.capitalize()}: {resources[key]}ml")
        elif key in itemsInGrams:
            print(f"{key.capitalize()}: {resources[key]}g")
        else:
            print(f"{key.capitalize()}: ${resources[key]}")

def insertCoins():
    print("Please insert coins.\n")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = round((quarters * 0.25) + (dimes * 0.10)+ (nickels * 0.05)+ (pennies * 0.01), 2)
    return total

def checkIngredientsAndMoney(requestedItem, money):
    for ingredient in MENU[requestedItem]['ingredients']:
        if resources[ingredient] < MENU[requestedItem]['ingredients'][ingredient]:
            return f"Sorry, there is not enough {requestedItem}."
    if money < MENU[requestedItem]['cost']:
        return f"Sorry, you need to insert more coins."
        
    return True;

def processOrder(requestedItem, money):
    for ingredient in MENU[requestedItem]['ingredients']:
        resources[ingredient] -= MENU[requestedItem]['ingredients'][ingredient]
    money -= MENU[requestedItem]['cost']
    money = round(money, 2)
    
    print(f"Here is ${money} in change.")
    print(f"Here is your {requestedItem}. Enjoy!")
    return MENU[requestedItem]['cost']

while coffeeMachineActive:
    requestedItem = input("What would you like? (espresso/latte/cappucino): ")
    if requestedItem == 'report':
        displayResources()
    if requestedItem == 'deactivate':
        print(f"Profit from today: ${round(profit,2)}.")
        coffeeMachineActive = False
    elif requestedItem in options:
        money = insertCoins()
        resultOfCheck = checkIngredientsAndMoney(requestedItem, money)
        if resultOfCheck == True:
            profit += processOrder(requestedItem, money)
        else:
            print(resultOfCheck)
    else:
        coffeeMachineActive = True
