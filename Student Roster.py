sr = ['Anya', 'Yagami', 'Uzumaki Naruto']
while True:
    ch = input("What change do you want to do to list?(add or remove or view or end)")
    if ch == 'add':
        sr.append(input("Enter the element you want to add"))
    elif ch == 'remove':
        sr.remove(input("Enter the element you want to remove"))
    elif ch == 'view':
        print(sr)
    elif ch == 'end':
        break
    else:
        print("Please select a valid action")