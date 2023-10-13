'''Write a program that prints numbers from 1 to N, but for multiples of 3, print "Fizz" instead of the number,
and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz."'''
n = int(input("Enter n value"))
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)