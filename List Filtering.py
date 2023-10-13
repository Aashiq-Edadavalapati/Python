'''Given a list of numbers, create a program that filters out even or odd numbers based on user choice.'''
num = []
n = int(input("Enter number of numbers you want to enter"))
for i in range(0, n):
    a = int(input("Enter a number"))
    num.append(a)
out = input("Do you want even or odd?")
if out == 'even':
    for i in range(0, n):
        if num[i] % 2 == 0:
            print(num[i])
else:
    for i in range(0, n):
        if num[i] % 2 != 0:
            print(num[i])