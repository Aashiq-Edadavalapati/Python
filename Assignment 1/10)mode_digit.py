'''Write a program mode_digit.py that takes an integer number num and returns the digit that appears most frequently in
that number. The given number may be positive or negative, but the most frequent digit returned should always be non-negative.
If there is a tie for the most frequent digit, the digit with the greatest value should be returned.'''

n = abs(int(input("Enter a number")))
count = [0]*10
print(count)
while n > 0:
    i = n % 10
    n = n//10
    count[i] += 1
max_count = max(count)
max_digit = count.index(max_count)
for i in range(0,10):
    if max_count == i:
        for j in range(i, 10):
            if count[j] == count[i]:
                max_digit = j
print(count)
print(max_digit)