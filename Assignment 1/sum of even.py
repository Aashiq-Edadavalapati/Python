'''You have a list of numbers, and you need to calculate the sum of all the even numbers. How would you do this?'''

num = [2,4,13,324,2456,5,1,32,24,1,234,3,897]
sum = 0
for i in num:
    if i % 2 == 0:
        sum = sum +i
print(sum)