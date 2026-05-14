import sys
def inputUsername():
    try:
        username = input("Input Username: ")
        return username
    except ValueError:
        print("Input Invalid!")
        return None, None
    except EOFError:
        print("[!]DANGER. Closing Program For Safety.")
        return 1
    except Exception:
        print("Fatal Error! Your Input Invalid")
        return 1

def inputPassword():
    try:
        passw = input("Input Password: ")
        return passw
    except ValueError:
        print("Input Invalid!")
        return None, None
    except EOFError:
        print("[!]DANGER. Closing Program For Safety")
        return 1
    except Exception:
        print("Fatal Error!")
        return 1

def exitUser():
    try:
        passw = input("Continue Or Exit(C/E): ")
        return passw
    except ValueError:
        print("Input Invalid!")
        return None, None
    except EOFError:
        print("[!]DANGER. Closing Program For Safety")
        return 1
    except Exception:
        print("Fatal Error!")
        return 1

dbUser = "California123"
dbPass = "California1234"
option = True

while (option):
    user = inputUsername()
    passw = inputPassword()

    if (user == dbUser and passw == dbPass):
        print("Good Night Sir. Welcome To California.")
        option = False
    else:
        print("Username Or Password Invalid")
    
    userChoice = exitUser()

    if (userChoice == "C"):
        continue
    elif (userChoice == "E"):
        option = False
    else:
        print("Input Invalid. Please input C / E")
    
