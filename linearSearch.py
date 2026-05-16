# ================================================================
# Project        : Mini Linear Search Program
# Language       : Python 3
# Author         : Novandy Triarto Wahyono
#
# Description:
# A simple terminal-based linear search implementation designed
# to practice core Python programming fundamentals including:
# input validation, exception handling, looping, modular function
# design, and basic search algorithms.
#
# Features:
# - Dynamic number input system
# - Linear search implementation
# - Defensive programming approach
# - Exception handling for invalid input and EOF conditions
# - Modular and readable function structure
#
# Concepts Practiced:
# - Functions
# - Lists
# - Loops
# - Enumerate
# - Error handling
# - Control flow
# - Search algorithms
#
# Notes:
# This project was built as part of a computer science and
# software engineering self-learning journey focused on
# problem-solving and programming fundamentals.
# ================================================================
import sys

#Input Number Function
def inputNumber():
    try:
        user = int(input("Input Number Or Choose 0 For Exit: "))
        return user
    except ValueError:
        print("Input Invalid. Please Input Normal Number")
        return None
    except EOFError:
        print("[!]DANGER. Closing Program For Safety.")
        return None
    except Exception as e:
        print(f"Fatal Error Because: {e}")
        return None

#Search Index Input
def inputIndex():
    try:
        user = int(input("Input Number For Search Index: "))
        return user
    except ValueError:
        print("Input Invalid. Please Input Normal Number")
        return None
    except EOFError:
        print("[!]DANGER. Closing Program For Safety")
        return None
    except Exception as e:
        print(f"Fatal Error Because: {e}")

#main Program
database = []
userInput = True

while (userInput):
    user = inputNumber()
    
    if (user is None):
        print("Input Cannot None")
        continue

    if (user == 0):
        userInput = False
    
    if (user < 0):
        print("Input Cannot Less Than Zero")
        continue

    database.append(user)

#Search Index
print("=============== SEARCH NUMBER INDEX ===============")
search = inputIndex()

if (search is not None):
    found = False

    for index, value in enumerate(database):
        if (search == value):
            print(f"Number {value} Is In Index: {index}")
            found = True
else :
    print("Input Not Found")



# ================================================================
# End of Program
#
# Future Improvements:
# - Implement binary search algorithm
# - Add sorting feature
# - Improve input abstraction and validation system
# - Refactor into class-based architecture
# - Add persistent data storage support
#
# Status:
# Completed as a beginner-to-intermediate level Python practice
# project focused on algorithmic thinking and software engineering
# fundamentals.
# ================================================================