
# Write your solution here
from datetime import datetime, timedelta
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
dob = datetime(year,month,day)
eve_of_new_mill = datetime(1999,12,31)
difference = eve_of_new_mill - dob 

if dob < eve_of_new_mill:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print(f"You weren't born yet on the eve of the new millennium.")