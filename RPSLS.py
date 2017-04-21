import time
from time import sleep
import random

end_of_game="_"*40
wins=0
losses=0
draws=0
legal_action=["rock","paper","scissors", "lizard", "Spock"]
while True:
    user_action=input("rock, paper, scissors, lizard, Spock: ")
    if user_action not in legal_action:
        print ("That is not a valid choice")
        continue
        
    computer_action=random.choice(legal_action)
    sleep(0.5)
    print (('Computer picked {}.').format(computer_action))
    if user_action == computer_action:
        sleep(0.5)
        draws += 1
        print (("\nIt's a draw.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "rock" and computer_action == "scissors":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Rock crushes scissors.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "paper" and computer_action == "rock":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Paper covers rock.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "scissors" and computer_action == "paper":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Scissors cuts paper.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "rock" and computer_action == "lizard":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Rock crushes lizard.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "lizard" and computer_action == "Spock":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Lizard poisons Spock.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "Spock" and computer_action == "scissors":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Spock smashes scissors.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "scissors" and computer_action == "lizard":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Scissors decapitate Lizard.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "lizard" and computer_action == "paper":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Lizard eats paper.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "paper" and computer_action == "Spock":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Paper disproves Spock.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    elif user_action == "Spock" and computer_action == "rock":
        sleep(0.5)
        wins += 1
        print (("\nYou win.  Spock vaporizes Rock.\n{}").format(end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
    else:
        sleep(0.5)
        losses += 1
        print (("\nYou lose. {} loses to {}\n").format(user_action, computer_action, end_of_game))
        print ("Your record is " + str(wins) + "-" + str(losses) + "-" + str(draws))
