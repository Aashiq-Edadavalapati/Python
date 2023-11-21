'''You have a tuple of numbers, and you need to find the median. How would you do this?'''
num = (1,4,20,2,30,7,98,45)
num = list(num)
num.sort()
n = len(num)
if n%2 == 0:
    median = (num[n//2-1]+num[n//2])/2
else:
    median = num[(n+1)//2-1]
num = tuple(num)
print(num)
print(median)