com = {'rock', 'paper', 'scissors'}
n = int(input("How many rounds do you want to play?"))
sc, su = 0, 0
for x in range(1,n+1):
    c = com.pop()
    com.add(c)
    user = input("Choose your option(rock or paper or scissors)")
    if ((c == 'rock' and user == 'scissors') or (c == 'paper' and user == 'rock') or (c == 'scissors' and user == 'paper')):
        print('Ooops you lost!')
        sc += 1
    elif ((c == 'rock' and user == 'paper') or (c == 'paper' and user == 'scissors') or (c == 'scissors' and user == 'rock')):
        print('Yay you won!')
        su += 1
    else:
        print("It's draw")
print()
if sc > su:
    print('Oops you lost the game!!')
elif su > sc:
    print("Yay you won the game!!")
else:
    print("The game is a draw!!")