n = input("Enter a word or phrase")
l = len(n)
j = l-1
c = 0
for i in range(0, l//2):
    if n[j] != n[i]:
        print(n, "is not a palindrome")
        break
    else:
        c += 1
    j -= 1
if c == l//2:
    print(n, "is a palindrome")