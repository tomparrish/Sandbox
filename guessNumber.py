import random

guessesTaken = 0

print('Pick a number between 1 and what number on the high end?')
range = input()
range = int(range)

print('How many guesses should I allow?')
guesses = input()
guesses = int(guesses)

number = random.randint(1,range)
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
