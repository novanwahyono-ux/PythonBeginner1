#mini program
import sys

#Input Number Fucntion
def userInput():
    try:
        user = int(input("INPUT NUMBER OR CHOOSE 0 FOR EXIT: "))
        return user
    except ValueError:
        print("INPUT INVALID. PLEASE INPUT NORMAL NUMBER")
        return None
    except EOFError:
        print("[!]DANGER. CLOSING PROGRAM FOR SAFETY")
        return None
    except Exception as e:
        print(f"FATAL ERROR BECAUSE: {e}")

#Ascending Sorting Function
def ascendingSort(database):
    size = len(database)
    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            if (database[j] > database[j + 1]):
                temp = database[j]
                database[j] = database[j + 1]
                database[j + 1] = temp
                swapped = True
        if (not swapped):
            break

#Descending Sorting Function
def descendingSort(database):
    size = len(database)
    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            if (database[j] < database[j + 1]):
                temp = database[j]
                database[j] = database[j + 1]
                database[j + 1] = temp
                swapped = True
        if (not swapped):
            break

#Display Sort
def displaySort(database):
    print("[ ", end=" ")
    for numb in database:
        print(numb, end=" ")
    print(" ]")

#Choice Function
def chooseOption():
    print("===============================")
    print("   PYTHON BUBBLE SORTING V1     ")
    print("===============================")
    print("1. INPUT A FOR ASCENDING SORT")
    print("2. INPUT D FOR DESCENDING SORT")
    print("3. INPUT E FOR EXIT")
    print("===============================")

    try:
        user = input("INPUT CHOICE: ")
    except ValueError:
        print("INPUT INVALID. PLEASE INPUT BETWEEN A, D, OR E")
        return None
    except EOFError:
        print("[!]DANGER. CLOSING PROGRAM FOR SAFETY.")
        return None
    except Exception as e:
        print(f"FATAL ERROR BECAUSE: {e}")
        return None

    user = user.upper()

    match (user):
        case 'A': return 'A'
        case 'D': return 'D'
        case 'E': return 'E'
        case _: print("INPUT INVALID.")

    return user

#Main Program
database = []
numberLoops = True
choiceLoops = True

#Input Number Loops
while (numberLoops):
    number = userInput()

    if (number is None):
        print("INPUT CANNOT ZERO")
        continue

    if (number == 0):
        break

    if (number < 0):
        print("INPUT CANNOT LESS THAN ZERO")
        continue

    database.append(number)
    print(f"USER COUNT: {len(database)}")

#Choice Loops
while (choiceLoops):
    choice = chooseOption()

    match (choice):
        case 'A':
            print("BEFORE ASCENDING SORT: ", end=" ")
            displaySort(database)
            ascendingSort(database)
            print("AFTER ASCENSING SORT: ", end=" ")
            displaySort(database)
        case 'D':
            print("BEFORE DESCENDING SORT: ", end=" ")
            displaySort(database)
            descendingSort(database)
            print("AFTER DESCENDING SORT: ", end=" ")
            displaySort(database)
        case 'E':
            print("EXITING PROGRAM")
            choiceLoops = False
        case _: 
            print("YOUR INPUT INVALID. TRY AGAIN BETWEEN A, D, OR E")
    
