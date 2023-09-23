"""
Please write a program which asks the user for a number of days. 
The program then prints out the number of seconds in the amount of days given.

The program should function as follows:
How many days? 1
Seconds in that many days: 86400
"""
seconds_perday = (60**2) * 24
seconds = seconds_perday * int(input("How many days? "))
print(f"Seconds in that many days: {seconds}")