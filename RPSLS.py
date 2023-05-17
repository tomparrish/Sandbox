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
legal_action=["rock","paper","scissors", "lizard", "Spock"]

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
while True:
    user_action=input("Select your action (rock, paper, scissors, lizard, Spock): ")
    if user_action not in legal_action:
        print ("That is not a valid choice")
        continue
        
    # computer selects action
    computer_action=random.choice(legal_action)
    thinking()
    print (('\nComputer picked {}.').format(computer_action))

    # which action wins (this can be shortened)
    if user_action == computer_action:
        thinking()
        draws += 1
        print ("\nIt's a draw.\n")
    elif user_action == "rock" and computer_action == "scissors":
        thinking()
        wins += 1
        print (("\nYou win.  Rock crushes scissors.\n"))
    elif user_action == "paper" and computer_action == "rock":
        thinking()
        wins += 1
        print ("\nYou win.  Paper covers rock.\n")
    elif user_action == "scissors" and computer_action == "paper":
        thinking()
        wins += 1
        print ("\nYou win.  Scissors cuts paper.\n")
    elif user_action == "rock" and computer_action == "lizard":
        thinking()
        wins += 1
        print ("\nYou win.  Rock crushes lizard.\n")
    elif user_action == "lizard" and computer_action == "Spock":
        thinking()
        wins += 1
        print ("\nYou win.  Lizard poisons Spock.\n")
    elif user_action == "Spock" and computer_action == "scissors":
        thinking()
        wins += 1
        print ("\nYou win.  Spock smashes scissors.\n")
    elif user_action == "scissors" and computer_action == "lizard":
        thinking()
        wins += 1
        print ("\nYou win.  Scissors decapitate Lizard.\n")
    elif user_action == "lizard" and computer_action == "paper":
        thinking()
        wins += 1
        print ("\nYou win.  Lizard eats paper.\n")
    elif user_action == "paper" and computer_action == "Spock":
        thinking()
        wins += 1
        print ("\nYou win.  Paper disproves Spock.\n")
    elif user_action == "Spock" and computer_action == "rock":
        thinking()
        wins += 1
        print ("\nYou win.  Spock vaporizes Rock.\n")
    else:
        thinking()
        losses += 1
        print (("\nYou lose. {} loses to {}\n").format(user_action, computer_action))
    printScore()
