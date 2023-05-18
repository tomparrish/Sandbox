# A command-line version of the well-known game: Rock, Paper, Scissors, Lizard, Spock.

# import dependencies
import time
from time import sleep
import random

# global variables
end_of_game="_"*40
wins=0
losses=0
draws=0
legal_action=["rock","paper","scissors", "lizard", "spock"]

# array to hold the rules of the game
rules = [
    ["scissors", ["cuts", "snips", "notches"], "paper"],
    ["paper", ["covers", "wraps", "veils"], "rock"],
    ["rock", ["crushes" "chokes", "kablooeys"], "lizard"],
    ["lizard", ["poisons", "bites", "claws"], "spock"],
    ["spock", ["smashes", "destroys", "wallops"], "scissors"],
    ["scissors", ["decapitates", "stabs", "cuts the head off of"], "lizard"],
    ["lizard", ["eats", "mutates and spits acid on", "claws"], "paper"],
    ["paper", ["disproves", "gives a nasty papercut to", "analyzes"], "spock"],
    ["spock", ["vaporizes", "decimates", "pulverizes"], "rock"],
    ["rock", ["crushes", "bend", "ruin"], "scissors"]]

# check the rules and determine who wins the round
def determineWinner(ua, ca):
    global wins, losses, draws
    salt = random.randint(1,3)
    if ua == ca:
        print ("\nIt's a draw.\n")
        draws += 1
    for i in rules:
        if i[0] == ua and i[2] == ca:
            print("\nYou win!", i[0], i[1][salt], i[2],"\n")
            wins += 1
        elif i[0] == ca and i[2] == ua:
            print("You lose!", i[0], i[1][salt], i[2], "\n") 
            losses += 1
    
# print current score
def printScore():
    print (("Current Score: " + str(wins) + "W / " + str(losses) + "L / " + str(draws) + "D\n{}\n").format(end_of_game))

# give the computer time to think
def thinking():
    for i in range(1,5):
        for cursor in '\\|/- ':
            time.sleep(0.1)
            print(f"\r{cursor}", end="", flush=True)

# main logic (should we add an option to quit?)
def main():
    while True:
        # ask user for input (how about we make this case insensitive or offer shortcuts?)
        user_action=input("Select your action (rock, paper, scissors, lizard, spock): ")
        if user_action not in legal_action:
            print ("That is not a valid choice")
            continue
        
        # computer selects action
        computer_action=random.choice(legal_action)
        thinking()
        print (('\nComputer picked {}.\n').format(computer_action))

        determineWinner(user_action, computer_action)
        printScore()
    
main()
