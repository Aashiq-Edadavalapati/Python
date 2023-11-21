# One morning, you go out and place a ten rupee note (whose thickness is 0.11mm) on the sidewalk by a tower
# (whose height is 442m) in your hometown. Each day thereafter, you go out and double the number of rupee notes.
# How long does it take for the stack of rupee notes to exceed the height of the tower?
# Write a program stack_rupee.py to calculate this.

tt, ht, d = 0.11, 442*1000, 0
while True:
    if tt <= ht:
        tt = tt * 2
        d += 1
    else:
        break
print(f'It will take {d} days to stack coins to a height greater than tower')