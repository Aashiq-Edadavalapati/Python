n = 30
i = int(input("Guess the number:"))
j = 0
while j == 0:
    if i == n:
        print("Yay! Correct")
        break
    elif i < n:
        print("Oops! too low")
        i = int(input())
    else:
        print("Oops! too high")
        i = int(input())