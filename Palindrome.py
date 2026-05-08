leaderboard = {
    "Jason": 1,
    "Jacob": 5,
    "Nicholas": 15,
    "Russell": 50,
    "Reza": 23
}

game = True
score = 0
streak = 0  # NEW: track consecutive correct answers


def printLeaderboard():
    for key, value in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True):
        print(f"{key}: {value}")


def playGame(score):
    global streak

    s = input("Enter a palindrome: ")

    if s == s[::-1]:
        print("Yes")
        score += 1
        streak += 1

        # NEW: streak bonus every 3 correct answers
        if streak % 3 == 0:
            print("Streak bonus! +2 points")
            score += 2

        globals()['score'] = score
    else:
        print("No")
        streak = 0  # reset streak on failure


def printMenu():
    print("Welcome to Palindrome")
    print("1. Play")
    print("2. See Leaderboard")
    print("3. Exit")


def handleUserInput(userInput, username):
    match userInput:
        case "1":
            playGame(score)
            return True
        case "2":
            printLeaderboard()
            return True
        case "3":
            print("Thanks for playing, " + username + "!, score: " + str(score))
            return False
        case _:
            print("Invalid Input, Please Try Again")
            return True


def getUserInput(username):
    printMenu()
    userInput = input("Make A Selection: ")
    return handleUserInput(userInput, username)


username = input("Enter Your Username: ")
while game:
    game = getUserInput(username)

leaderboard[username] = score

printLeaderboard()
