left, right = 1, 100
while left <= right:
    mid = (left+right)//2
    result = input(f'Is the number {mid}?(Y/N)').lower()
    if result == 'y':
        print(f'The number you are thinking is {mid}')
        break
    elif result == 'n':
        result = input(f'Is your number greater than {mid}?(y/n)')
        if result == 'y':
            left = mid+1
        elif result == 'n':
            right = mid-1
    else:
        print('choose a correct option')
