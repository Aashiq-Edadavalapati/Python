'''To-Do List: Create a to-do list where users can add tasks, mark them as complete, and
view their current tasks.'''
todo_list = []
while True:
    print("Select your choice number from the below mentioned options:")
    print(' 1)Add a new task.')
    print(' 2)Mark a task as completed.')
    print(' 3)View your current tasks.')
    print(' 4)Quit')
    choice = int(input('Enter your choice(1/2/3/4):'))
    if choice == 1:
        task = input('Enter the task:')
        todo_list.append([task,False])
    elif choice == 2:
        print('Your present tasks:')
        for i in range(len(todo_list)):
            status = 'X' if todo_list[i][1] else ''
            print(f'{i+1}){todo_list[i][0]}[{status}]')
        comp = int(input('Choose the number of the completed task:'))
        todo_list[i][1] = True
    elif choice == 3:
        print('Your present tasks:')
        for i in range(len(todo_list)):
            status = 'X' if todo_list[i][1] else ''
            print(f'{i + 1}){todo_list[i][0]}[{status}]')
    elif choice == 4:
        break
    else:
        print('Please select a valid option!')