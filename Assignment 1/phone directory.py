''' Create a phone directory where users can add, search for, and delete contacts using dictionaries. '''
directory = {}
while True:
    print("Select your choice number from the below mentioned options:")
    print(' 1)Add a new contact.')
    print(' 2)Delete a contact.')
    print(' 3)Search for a contact.')
    print(' 4)Quit')
    choice = int(input('Enter your choice(1/2/3/4):'))
    if choice == 1:
        contact = input('Enter the contact')
        name = input('Enter the name of the contact')
        directory.update({name: contact})
    elif choice == 2:
        name = input('Enter the name of the contact you want to remove ')
        directory.pop(name)
    elif choice == 3:
        name = input('Enter the name of the contact you want to search for')
        print(directory[name])
    elif choice == 4:
        break
    else:
        print('Choose a valid option')