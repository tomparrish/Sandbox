# A Hangman style program that uses m-w.com's word of the day
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

soup = BeautifulSoup(urlopen("https://www.merriam-webster.com/word-of-the-day"), "lxml")
phrase = soup.title.string
word = phrase.split()[4]
word = word.lower()
guesses = ''
turns = 10

print ("Guess mw.com's Word of the Day")
print ("")
time.sleep(0.5)

print ("I'll give you 10 guesses.")
time.sleep(0.5)

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print (char),
        else:
            print ("_"),
            failed += 1
    if failed == 0:
        print ("You win!")
        break
        
    print
    guess = input("guess!")
    guess = guess.lower()
    guesses += guess
    if guess not in word:
            turns -= 1
            print ("Wrong")
            print ("You have", + turns, 'more guesses')
            if turns == 0:
                print ("You lose")
                
