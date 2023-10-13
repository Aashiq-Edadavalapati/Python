'''Write a program that takes a student's score as input and prints their grade.
 Use a grading scale (e.g., A, B, C, D, F) based on their score.'''
score = int(input("Enter the score:"))
if score >= 90:
    print("A grade")
elif score >= 75:
    print("B grade")
elif score >= 55:
    print("C grade")
elif score >= 30:
    print("D grade")
else:
    print("F grade")