"""
Please write a program which asks the user for an integer number. 
The program should then print out the magnitude of the number according to the following examples.

Please type in a number: 950
This number is smaller than 1000
Thank you!

Please type in a number: 2
This number is smaller than 1000
This number is smaller than 100
This number is smaller than 10
Thank you!

Please type in a number: 1123
Thank you!
"""

number = int(input("Please type in a number: "))
MAX_NUMBER = 1000
MIN_NUMBER = 10
MID_NUMBER = 100
message = "This number is smaller than "
value = 0
# check for max number
if number < MAX_NUMBER:
    print(f"{message}{MAX_NUMBER}")
# check for mid number
if number < MID_NUMBER:
    print(f"{message}{MID_NUMBER}")
# check for min number
if number < MIN_NUMBER:
    print(f"{message}{MIN_NUMBER}")
print("Thank you!")

