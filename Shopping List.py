sl = ['Food','Clothes','Accessories']
while True:
    ch = input("What change do you want to do to list?(add or remove or view or end)")
    if ch == 'add':
        sl.append(input("Enter the element you want to add"))
    elif ch == 'remove':
        x = input("Enter the element you want to remove")
        sl.remove(x)
    elif ch == 'view':
        print(sl)
    elif ch == 'end':
        break
    else:
        print("Please select a valid action")