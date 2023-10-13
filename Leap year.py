n = int(input("Enter a year"))
if n % 100 == 0:
    if n % 400 == 0:
        print(n, "is a leap year")
    else:
        print(n, "is not a leap year")
else:
    if n % 4 == 0:
        print(n, "is a leap year")
    else:
        print(n, "is not a leap year")