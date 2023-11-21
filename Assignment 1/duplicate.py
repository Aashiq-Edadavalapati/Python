'''You have a list of words, and you need to remove all the duplicate words. How would you do this?'''
word = ['hatake','hyuga','uzumaki','uchiha','uchiha','hyuga']
saw = []
unique = []
for i in word:
    if i not in saw:
        unique.append(i)
        saw.append(i)
print(unique)