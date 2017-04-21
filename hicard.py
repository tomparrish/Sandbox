import random

suits = ["spades", "hearts", "clubs", "diamonds"]
ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

def randomcard():
    card = random.choice(ranks) + " of " + random.choice(suits)
    return card

def main():
    playercard = randomcard()
    computercard = randomcard()
    print ("Your card is " + playercard)
    print ("My card is " + computercard)
    
main()
