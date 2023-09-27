from array import *
n = array('i', [23, 3, 12, 26, 75])
for e in range(0, len(n)):
    for f in range(e+1, len(n)):
        if n[e] > n[f]:
            t = n[e]
            n[e] = n[f]
            n[f] = t
for i in range(0, len(n)):
    print(n[i], end=" ")
