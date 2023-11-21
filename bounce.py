#A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5th of
#the height it fell. Write a program bounce.py that prints a table showing the height of the first 10 bounces.
# Try to round the output to 4 significant digits.

h = 100
for i in range(1,11):
    bh = 3 *h/5
    h = bh
    print(bh)