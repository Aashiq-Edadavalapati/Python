'''Create a program that converts a decimal number into binary, octal, or hexadecimal based on user choice.'''
n = int(input("Enter a decimal number"))
typ = input("Enter type you want to convert it to(binary,octal,hexadecimal):")
if typ == 'binary':
    print(bin(n))
elif typ == 'octal':
    print(oct(n))
else:
    print(hex(n))