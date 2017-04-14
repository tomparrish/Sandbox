import time
from time import sleep
import random

endOfGame="_"*40
wins=0
losses=0
draws=0
legalAction=["rock","paper","scissors", "lizard", "Spock"]
while True:
    userAction=input("rock, paper, scissors, lizard, Spock: ")
    if userAction not in legalAction:
        print ("That is not a valid choice")
        continue
        
    computerAction=random.choice(legalAction)
    sleep(0.5)
    print (('Computer picked {}.').format(computerAction))
    if userAction == computerAction:
        sleep(0.5)
        draws += 1
        print (("\nIt's a draw.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "rock" and computerAction == "scissors":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Rock crushes scissors.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "paper" and computerAction == "rock":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Paper covers rock.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "scissors" and computerAction == "paper":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Scissors cuts paper.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "rock" and computerAction == "lizard":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Rock crushes lizard.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "lizard" and computerAction == "Spock":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Lizard poisons Spock.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "Spock" and computerAction == "scissors":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Spock smashes scissors.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "scissors" and computerAction == "lizard":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Scissors decapitate Lizard.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "lizard" and computerAction == "paper":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Lizard eats paper.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "paper" and computerAction == "Spock":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Paper disproves Spock.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif userAction == "Spock" and computerAction == "rock":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Spock vaporizes Rock.\n{}").format(endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    else:
        sleep(0.5)
        losses += 1
        print (("\nYou lose. {} loses to {}\n").format(userAction, computerAction, endOfGame))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
