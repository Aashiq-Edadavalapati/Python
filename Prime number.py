n = int(input("Enter a number"))
count = 0
for i in range(2, (n//2)):
    if n % i == 0:
        count += 1
if count != 0:
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")

