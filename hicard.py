import random
from time import sleep

suits = ["spades", "hearts", "clubs", "diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
rankvalues = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":15, "Queen":20, "King":25, "Ace":100}

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
    else:
        comment = "ho-hum"
    return comment

def getcardvalue(card):
        value = rankvalues.get(card.partition(' ')[0])
        return value

def whowon(playercard, computercard):
    playervalue = getcardvalue(playercard)
    computervalue = getcardvalue(computercard)
    if playervalue > computervalue:
        result = "You won!"
    elif playervalue < computervalue:
        result = "I won!"
    elif playercard in computercard:
        result = "Reach for the sky hombre, someone is trying to pull a fast one here."
    else:
        result = "It's like kissing your sister!"
    return result

def main():
    playercard = randomcard()
    computercard = randomcard()
    comment = commentary(playercard)
    result = whowon(playercard, computercard)
    print ("Your card is " + playercard)
    sleep(0.5)
    print ()
    print (comment)
    print ()   
    sleep(0.5)
    print ("My card is " + computercard)
    sleep(0.5)
    print (result)
    sleep(2)
    
main()
