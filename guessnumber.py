import random

def get_range():
    print('Pick a number between 1 and what number on the high end?')
    range = input()
    range = int(range)
    return range
    
def get_guesses():
    print('How many guesses should I allow?')
    guesses = input()
    guesses = int(guesses)
    return guesses
    
def get_number(range):
    number = random.randint(1,range)
    return number

def main_loop(range, guesses, number, guesses_taken):
    guess = 0
    print('I am thinking of a number between 1 and ' + str(range))
    while guesses_taken < guesses:
        print('Take a guess.')
        guess = input()
        guess = int(guess)
        guesses_taken = guesses_taken + 1    
        if guess < number:
            print('Your guess is too low.')
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            break
    if guess == number:
        guesses_taken = str(guesses_taken)
        print('You guessed my number in ' + guesses_taken + ' guesses!')
    if guess != number:
        number = str(number)
        print ('Nope.  The number I was thinking of was ' + number)
        
#def main():
global range
global guesses
global number
global guesses_taken
range = get_range()
guesses = get_guesses()
number = get_number(range)
guesses_taken = 0
main_loop(range, guesses, number, guesses_taken)
