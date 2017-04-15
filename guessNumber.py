import random

def getRange():
    print('Pick a number between 1 and what number on the high end?')
    range = input()
    range = int(range)
    return range
    
def getGuesses():
    print('How many guesses should I allow?')
    guesses = input()
    guesses = int(guesses)
    return guesses
    
def getNumber(range):
    number = random.randint(1,range)
    return number

def mainLoop(range, guesses, number, guessesTaken):
    guess = 0
    print('I am thinking of a number between 1 and ' + str(range))
    while guessesTaken < guesses:
        print('Take a guess.')
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1    
        if guess < number:
            print('Your guess is too low.')
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('You guessed my number in ' + guessesTaken + ' guesses!')
    if guess != number:
        number = str(number)
        print ('Nope.  The number I was thinking of was ' + number)
        
#def main():
global range
global guesses
global number
global guessesTaken
range = getRange()
guesses = getGuesses()
number = getNumber(range)
guessesTaken = 0
mainLoop(range, guesses, number, guessesTaken)
