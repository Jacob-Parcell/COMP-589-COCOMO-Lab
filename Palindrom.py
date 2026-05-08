def playGame():
    s = input("Enter a palindrome: ") 
    i, j = 0, len(s) - 1  
    is_palindrome = True  

    if s == s[::-1]:
        print("Yes")
    else:
        print("No")


def printMenu():
    print("Welcome to Palindrome")
    print("1. Play")
    print("2. See Leaderboard")
    print("3. Exit")

def handleUserInput(userInput):
    match userInput:
        case "1":
            playGame()
        case "2":
            printLeaderboard()
        case "3":
            endLoop()
        case _:
            print("Invalid Input, Please Try Again")

def getUserInput():
    printMenu()
    userInput = input("Make A Selection: ") 
    handleUserInput(userInput)

getUserInput()
