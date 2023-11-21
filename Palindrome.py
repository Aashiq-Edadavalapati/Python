n = input("Enter a word or phrase")
l = len(n)
j = l-1
c = True
for i in range(0, l//2):
    if n[j] != n[i]:
        print(n, "is not a palindrome")
        c = False
        break
    else:
        c = True
    j -= 1
if c == True:
    print(n, "is a palindrome")