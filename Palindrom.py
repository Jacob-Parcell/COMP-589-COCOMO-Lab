leaderboard = {
    "Jason" : 1,
    "Jacob" : 5,
    "Nicholas" : 15,
    "Russell" : 50,
    "Reza" : 23
}

def printLeaderboard():
    for key, value in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True):
        print(f"{key}: {value}")

def playGame():
    s = input("Enter a palindrome: ") 
    i, j = 0, len(s) - 1  
    is_palindrome = True  

    if s == s[::-1]:
        print("Yes")
        score += 1
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
            print("Thanks for playing!, score: " + str(score))
        case _:
            print("Invalid Input, Please Try Again")

game = True
score = 0

while game:
    def getUserInput():
        printMenu()
        userInput = input("Make A Selection: ") 
        handleUserInput(userInput)

getUserInput()
