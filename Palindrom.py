s = input("Enter a palindrome: ") 
i, j = 0, len(s) - 1  
is_palindrome = True  

while i < j:
    if s[i] != s[j]:  
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes") 
else:
    print("No")


def printMenu():
    print("Welcome to Palindrome")
    print("1. Play")
    print("2. See Leaderboard")
    print("3. Exit")