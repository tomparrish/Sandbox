# A Hangman style program that uses m-w.com's word of the day
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

def getword():
    soup = BeautifulSoup(urlopen("https://www.merriam-webster.com/word-of-the-day"), "lxml")
    phrase = soup.title.string
    word = phrase.split()[4]
    word = word.lower()
    return word

def intro_to_game():
    print ("Guess mw.com's Word of the Day")
    print ("")
    time.sleep(0.5)
    print ("I'll give you 10 guesses.")
    time.sleep(0.5)

def play(word):
    guesses = ''
    turns = 10
    while turns > 0:
        failed = 0
        drawFigure(turns)
        for char in word:
            if char in guesses:
                print (char, end = ""),
            else:
                print ("_ ", end = ""),
                failed += 1
        print()
        print ("Your guesses so far: " + guesses)
        if failed == 0:
            print ("You win!")
            break
        print()
        guess = input("guess! ")
        guess = guess.lower()
        guesses += guess
        print()
        if guess not in word:
                turns -= 1
                print ("Wrong")
                print ("You have", + turns, 'more guesses')
                print()
    return turns

def drawFigure(turns):
    body_parts = ["  |   O", "  |   |", "  |  /|", "  |  /|\\", "  |  /", "  |  / \\"]
    empty_scaffold = ["  +---+\n  |   |", "  |", "  |\n========="]
    print(empty_scaffold[0])
    match turns:
        case 5:
            print(body_parts[0], empty_scaffold[1], empty_scaffold[1],sep='\n')
        case 4:
            print(body_parts[0],body_parts[1], empty_scaffold[1],sep='\n')
        case 3:
            print(body_parts[0],body_parts[2], empty_scaffold[1],sep='\n')
        case 2:
            print(body_parts[0],body_parts[3], empty_scaffold[1],sep='\n')
        case 1:
            print(body_parts[0],body_parts[3],body_parts[4],sep='\n')
        case 0:
            print(body_parts[0],body_parts[3],body_parts[5],sep='\n')    
        case _:
            print(empty_scaffold[1],empty_scaffold[1],empty_scaffold[1],sep='\n')
    print(empty_scaffold[2])


def endgame(turns, word):
    if turns == 0:
        drawFigure(turns)
        print ("say uncle if you would like to see the word")
        answer=input()
        if "uncle" in answer.lower():
            print()
            print("M-W's Word of the Day is: " + word)
            print()        

def main():
    word = getword()
    intro_to_game()
    turns = play(word)
    endgame(turns,word)
    
main()
