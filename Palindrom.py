leaderboard = {
    "Jason" : 1,
    "Jacob" : 5,
    "Nicholas" : 15,
    "Russell" : 50,
    "Reza" : 23
}

game = True
score = 0

def printLeaderboard():
    for key, value in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True):
        print(f"{key}: {value}")

def playGame(score):
    s = input("Enter a palindrome: ") 
    i, j = 0, len(s) - 1  
    is_palindrome = True  

    if s == s[::-1]:
        print("Yes")
        score += 1
        globals()['score'] = score
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
            playGame(score)
            return True
        case "2":
            printLeaderboard()
            return True
        case "3":
            print("Thanks for playing!, score: " + str(score))
            return False
        case _:
            print("Invalid Input, Please Try Again")
            return True
        

def getUserInput():
    printMenu()
    userInput = input("Make A Selection: ") 
    return handleUserInput(userInput)

while game:
    game = getUserInput()


