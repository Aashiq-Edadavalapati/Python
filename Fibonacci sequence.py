n = int(input("Enter number of elements"))
i = 0
j = 1
print(i, j, end=" ")
for k in range(3, n+1):
    l = i + j
    print(l, end=" ")
    i = j
    j = l