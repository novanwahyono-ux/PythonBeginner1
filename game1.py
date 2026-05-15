"""
Rock Scissors Paper Game

A terminal-based Python game implementing:
- input validation
- exception handling
- modular programming
- randomized game logic

Author: Novandy Triarto Wahyono
"""
import sys
import random

def getUser():
    print("===================================")
    print("             WELCOME TO            ")
    print("PYTHON ROCK SCISSORS AND PAPER GAME")
    print("===================================")
    print("1. INPUT R FOR ROCK")
    print("2. INPUT S FOR SCISSORS")
    print("3. INPUT P FOR PAPER")
    print("===================================")

    try:
        option = input("CHOOSE OPTION: ")
    except ValueError:
        print("INPUT INVALID. PLEASE INPUT NORMAL CHARACKTER")
        return None
    except EOFError:
        print("[!]DANGER. CLOSING PROGRAM FOR SAFETY")
        return None
    except Exception:
        print("FATAL ERORR!")
        return None
    option = option.upper()

    match option:
        case 'R': return 'R'
        case 'S': return 'S'
        case 'P': return 'P'
        case _: print("YOUR INPUT INVALID")
    
    return option

def getComputer():
    number = random.randint(1, 3)
    match number:
        case 1: return 'R'
        case 2: return 'S'
        case 3: return 'P'
        case _: print("COMPUTER INPUT INVALID")
    return number

def showChoice(choice):
    match choice:
        case 'R': print("ROCK") 
        case 'S': print("SCISSORS") 
        case 'P': print("PAPER") 
        case _: print("UNKNOWN")

def chooseWinner(player, computer):
    if player == computer:
        print("DRAW")
    elif (player == 'R' and computer == 'S') or (player == 'S' and computer == 'P') or (player == 'P' and computer == 'R'):
        print("CONGATULATION SIR!!! YOU WIN THIS GAME")
    else:
        print("COMPUTER WIN!!! YOU LOSE THIS GAME SIR")

def exitUser():

    try:
        option = input("Input C For Continue Or E For Exit: ")
    except ValueError:
        print("INPUT INVALID. PLEASE INPUT NORMAL CHARACKTER")
        return None
    except EOFError:
        print("[!]DANGER. CLOSING PROGRAM FOR SAFETY")
        return None
    except Exception:
        print("FATAL ERROR!")
        return None
    
    option = option.upper()

    match option:
        case 'C': return 'C'
        case 'E': return 'E'
        case _: print("INPUT INVALID")

    return option

player = None
playAgain = None
exitOption = True

while (exitOption):
    computer = getComputer()
    while (True):
        player = getUser()
        if (player == 'R' or player == 'S' or player == 'P'):
            break
        else:
            continue
    
    
    print("USER CHOICE: ")
    showChoice(player)

    print("COMPUTER CHOICE: ")
    showChoice(computer)

    chooseWinner(player, computer)

    playAgain = exitUser()

    match playAgain:
        case 'C':
            continue
        case 'E':
            print("EXITING PROGRAM")
            exitOption = False

print("THANKYOU FOR USE OUR ECOSYSTEM")




# ============================================================
# Project : Rock Scissors Paper Game
# Language: Python 3
#
# Features:
# - User input validation
# - Exception handling (EOFError, invalid input, general exception)
# - Randomized computer choice using Python random module
# - Match-case implementation (Python 3.10+)
# - Game loop system
# - Basic defensive programming approach
#
# Concepts Practiced:
# - Functions
# - Conditional logic
# - While loops
# - Error handling
# - Input sanitization
# - Control flow management
#
# Author:
# Novandy
#
# Notes:
# This project was built as part of Python fundamentals practice
# focused on clean control flow, modular function design,
# and beginner-level software engineering principles.
# ============================================================





