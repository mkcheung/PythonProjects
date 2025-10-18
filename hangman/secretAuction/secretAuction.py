### The goal is to build a blind auction program. 

### Demo
###https://appbrewery.github.io/python-day9-demo/

### Clearing the Output
###There are several ways of clearing the output. The easiest is to simply print `"\n"` many times so that the output scrolls down many lines.

###e.g.
######```
# This will add 20 new lines to the output
###print("\n" * 20)
###```


### Functionality
###- Each person writes their name and bid.
###- The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
###- Each person's name and bid are saved to a dictionary.
###- Once all participants have placed their bid, the program works out who has the highest bid and prints it.

###  Try writing out a flowchart to plan your program.

###  The values that come from the input() function are Strings, you'll need to use the int() function to convert it to a number.
import art

print(art.logo)

bidderDict = {}

active = True

while active:
    name = input("Please enter name of bidder: ")
    bid = int(input("Please enter the bid amount: $"))
    bidderDict[name] = bid
    keepGoing = input("Do you want to enter another bidder? Please enter 'Yes' or 'No'. \n")
    if(keepGoing == 'No'):
        active = False
    print("\n" * 20)

def getBiggestBid(bigDict):
    bestBid = 0
    bestBidder = ''
    for key in bidderDict:
        if bidderDict[key] > bestBid:
            bestBidder = key
            bestBid = bidderDict[key]
    print(f"Best Bid by {bestBidder} at ${bestBid}")

getBiggestBid(bigDict=bidderDict)