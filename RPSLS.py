# A command-line version of the well-known game: Rock, Paper, Scissors, Lizard, Spock.

# import dependencies
import time
from time import sleep
import random

# array to hold the rules of the game
rules = [
    ["scissors", ["cuts", "snips", "notches"], "paper"],
    ["paper", ["covers", "wraps", "veils"], "rock"],
    ["rock", ["crushes", "chokes", "kablooeys"], "lizard"],
    ["lizard", ["poisons", "bites", "claws"], "spock"],
    ["spock", ["smashes", "destroys", "wallops"], "scissors"],
    ["scissors", ["decapitates", "stabs", "cuts the head off of"], "lizard"],
    ["lizard", ["eats", "mutates and spits acid on", "claws"], "paper"],
    ["paper", ["disproves", "gives a nasty papercut to", "analyzes"], "spock"],
    ["spock", ["vaporizes", "decimates", "pulverizes"], "rock"],
    ["rock", ["crushes", "bend", "ruin"], "scissors"]]
legal_action=["rock","paper","scissors", "lizard", "spock"]

# check the rules and determine who wins the round
def determineWinner(ua, ca, record):
    salt = random.randint(0,2)
    if ua == ca:
        print ("It's a draw.\n")
        record[2] += 1
    for i in rules:
        if i[0] == ua and i[2] == ca:
            print("You win!", i[0], i[1][salt], i[2],"\n")
            record[0] += 1
        elif i[0] == ca and i[2] == ua:
            print("You lose!", i[0], i[1][salt], i[2], "\n") 
            record[1] += 1
    return (record)
    
# print current score
def printScore(record):
    end_of_game="_"*40
    print (("Current Score: " + str(record[0]) + "W / " + str(record[1]) + "L / " + str(record[2]) + "D\n{}\n").format(end_of_game))

# give the computer time to think
def thinking():
    for i in range(1,5):
        for cursor in '\\|/- ':
            time.sleep(0.1)
            print(f"\r{cursor}", end="", flush=True)
   
# ask user for input
def useraction():
        user_action=input("Select your action ([r]ock, [p]aper, [s]cissors, [l]izard, spoc[k]): ")
        user_action = user_action.lower()
        match user_action:
            case "r":
                user_action = "rock"
            case "p":
                user_action = "paper"
            case "s":
                user_action = "scissors"
            case "l":
                user_action = "lizard"
            case "k":
                user_action = "spock"
        if user_action not in legal_action:
            print ("That is not a valid choice")
#            continue
        return(user_action)

# main logic (should we add an option to quit?)
def main():
    record = [0, 0, 0] # wins, losses, draws

    while True:
        user_action = useraction()
        
        # computer selects action
        computer_action=random.choice(legal_action)
        thinking()
        print (('\nComputer picked {}.\n').format(computer_action))

        determineWinner(user_action, computer_action, record)
        printScore(record)
    
main()
