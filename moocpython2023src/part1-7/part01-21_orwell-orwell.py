"""
Please write a program which asks the user for an integer number. 
The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.
Please type in a number: 2020
Please type in a number: 1984
Orwell
"""

year = int(input("Please type in a number: "))
orwell = 1984
if year == orwell:
    print("Orwell")