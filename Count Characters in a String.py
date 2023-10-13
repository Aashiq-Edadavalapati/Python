''' Write a program that counts the number of occurrences of a specific character in a given string.'''
n = input("Enter a string")
a = input("Enter the character you want to check")
c = 0
for i in range(0,len(n)):
    if n[i] == a:
        c += 1
print(a, "is occured", c, "times in", n)