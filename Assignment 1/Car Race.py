'''. Using a Python program, simulate a simple car race where cars move along a straight track. The cars have different
starting positions and speeds, and they move forward based on a series of time steps. Your goal is to determine which car
reaches the finish line first. The racetrack is straight, and cars move only in one direction (towards the finish line).Time
measurement is to be done in discrete time steps. Each car's position is represented as an integer (measured in meters from
the start line), and the speed is represented as an integer (measured in meters per time step). The finish line is located at
a fixed distance (say, 50 meters) from the start line. You may assume that the speed remains constant for the entire duration of
the race. [15 marks] [CO2] [BTL3]
a. Initialize two cars with their positions and speeds as variable properties. (5 marks)
Example:
• Car 1 starts at position 0 meters and has a speed of 2 meters per time step.
• Car 2 starts at position 10 meters and has a speed of 3 meters per time step.
b. Simulate the movement of the two cars until either one car overtakes the other, or one (or both) of the cars reach the
 finish line. Update the positions of the cars based on their speeds and print the output for each time step. (5 marks)
c. Determine which car wins the race. The car that overtakes the other before the finish line or the one that crosses the
finish line first wins. If both cars finish at the same time, consider it a tie. (5 marks)
Sample Input:
Each line of the input contains information about a car, consisting of three numbers: the
car number, its position from the starting point, and its speed in meters per second.
1 0 3
2 10 2
Sample Output:
Display the positions of each car until either one car overtakes the other or one (or both) of the cars reach the finish line.
Each line of the output starts with the car number and is followed by the positions that they are in during a measurement.
The display can stop as soon as a winner is decided, and the next position can be marked as ‘Winner’ or ‘Runner-up’.
1 0 3 6 9 12 15 18 21 24 27 30 33 Winner
2 10 12 14 16 18 20 22 24 26 28 30 32 Runner-Up'''
car_no1, position1, speed1 = map(int,input().split())
car_no2, position2, speed2 = map(int,input().split())
front, back = 0, 0
if position2 > position1:
    front = position2
    back = position1
elif position1 > position2:
    front = position1
    back = position2
post1, post2 = [position1], [position2]
if front == position1 and back == position2:
    while (front > back) and (position1 < 50 and position2 < 50):
        front, back = position1+speed1, position2+speed2
        post1.append(front)
        post2.append(back)
else:
    while (front > back) and (position1 < 50 and position2 < 50):
        front, back = position2 + speed2, position1 + speed1
        post1.append(back)
        post2.append(front)
for i in post1:
    print(i,end=' ')
if (position1>position2)or(position1>=50):
    print('Winner')
else:
    print('Runner-Up')
for j in post2:
    print(j,end=' ')
if (position2>position1)or(position2>=50):
    print('Winner')
else:
    print('Runner-Up')