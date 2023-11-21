x = [0]
y = [0]
i = D = 0
while i < 4:
    direction = input()
    dis = int(direction[-1])
    direction = direction[:-1]
    if direction == 'UP' or direction == 'U':
        x.append(x[i])
        y.append(y[i]+dis)
    elif direction == 'DOWN' or direction == 'D':
        x.append(x[i])
        y.append(y[i]-dis)
    elif direction == 'RIGHT' or direction == 'R':
        x.append(x[i]+dis)
        y.append(y[i])
    elif direction == 'LEFT' or direction == 'L':
        x.append(x[i]-dis)
        y.append(y[i])
    else:
        print('Enter a valid displacement')
    D = D + abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
    i += 1
print(x, y)
print(D)