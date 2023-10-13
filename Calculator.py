n = input("Enter arithmetic operation you want to perform: ")
a, b = map(float, input("Enter two numbers").split())
if n == '+':
    print(a+b)
if n == '-':
    print(a-b)
if n == '*':
    print(a*b)
if n == '/':
    print(a/b)