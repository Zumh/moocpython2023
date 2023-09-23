"""
Generally, any year that is divisible by four is a leap year. 
However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

Some examples:

Sample output
Please type in a year: 2011
That year is not a leap year.
"""

year = int(input("Please type in a year: "))

is_leap = False 

final_message = "That year is not a leap year."

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    final_message = "That year is a leap year."
print(final_message)


