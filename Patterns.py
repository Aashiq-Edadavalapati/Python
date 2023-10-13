'''Print a Pattern:
   Write a program to print a specific pattern using nested loops.
   For example, print a right-angled triangle, a square, or a diamond pattern.'''
print("1)right-angled triangle")
n = int(input("Enter number of rows"))
for i in range(0, n+1):
    for j in range(0, i):
        print("*", end=" ")
    print()
print("2)square")
n = int(input("Enter number of rows:"))
for i in range(0, n):
    for j in range(0, n):
        print("*", end=" ")
    print()
print("3)diamond")
n = int(input("Enter number of rows"))
for i in range(0, n):
    for j in range(0, n-i):
        print("", end=" ")
    for k in range(0, i):
        print("*")
    print()
for i in range(n+1, 0, -1):
    for j in range(0, n+1-i):
        print("",end=" ")
    for k in range(0, i):
        print("*", end=" ")
    print()
