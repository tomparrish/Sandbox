import random
from time import sleep

suits = ["spades", "hearts", "clubs", "diamonds"]
ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

def randomcard():
    card = random.choice(ranks) + " of " + random.choice(suits)
    return card
    
def commentary(playercard):
    comment = ""
    if "Ace of spades" in playercard:
        comment = "The Ace of spades!"
    elif "Ace" in playercard:
        comment = "He's got the Ace!"
    elif "King of hearts" in playercard or "King of diamonds" in playercard:
        comment = "Don't do it!  Life is worth living!  (Suicide King)"
    elif "King" in playercard:
        comment = "Cowboy Up!"
    return comment

def main():
    playercard = randomcard()
    computercard = randomcard()
    print ("Your card is " + playercard)
    print ("My card is " + computercard)
    sleep(0.5)
    comment = commentary(playercard)
    print (comment)
    
main()
