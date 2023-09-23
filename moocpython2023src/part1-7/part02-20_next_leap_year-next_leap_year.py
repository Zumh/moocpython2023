"""
Please write a program which asks the user for a year, and prints out the next leap year.
Year: 2023
The next leap year after 2023 is 2024

if year is leap year
Year: 2024
The next leap year after 2024 is 2028
"""

year = int(input("Year: "))
next_leap = year
found_next_leap = False 

while found_next_leap == False:
    next_leap += 1
    # check if year is leap year
    # detect leap year 
    if (next_leap % 4 == 0 and next_leap % 100 != 0) or (next_leap % 400 == 0):
        # find the next leap year 
        found_next_leap = True

print(f"The next leap year after {year} is {next_leap}")
