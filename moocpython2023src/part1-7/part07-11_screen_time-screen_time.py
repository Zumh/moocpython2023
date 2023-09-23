# Write your solution here

from datetime import datetime, timedelta


if True:
    filename = input("Filename: ")
    start_date = input("Starting date: ")
    input_days = int(input("How many days: "))
else:
    filename = "late_june.txt"
    start_date = "24.6.2020"
    input_days = 2

counting_day = 0
screen_time = {}
start_date = datetime.strptime(start_date,"%d.%m.%Y")
print(f"Please type in screen time in minutes on each day (TV computer mobile):")
formatted_date = start_date
while counting_day < input_days:
    screen_date = formatted_date.strftime("%d.%m.%Y")

    # extract screen time from the string
    current_screen_time = input(f"Screen time {screen_date}: ")
    

    screen_time[screen_date] = current_screen_time
    
    formatted_date += timedelta(days=1)
    counting_day += 1

with open(filename,"w") as myfile:
    # format the date 
    total_minutes = 0
    # calculate total minutes
    for screen_date in screen_time:
        for minute in screen_time[screen_date].split(" "):
            total_minutes += int(minute)

    # calculate average minutes
    average_minutes = total_minutes/input_days

    end_date = start_date + timedelta(days=input_days-1)


    result = f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\nTotal minutes: {total_minutes}\nAverage minutes: {average_minutes:.1f}\n"
    for screen_date in screen_time:
        formatted_minutes = screen_time[screen_date].replace(" ", "/")
        result += f"{screen_date}: {formatted_minutes}\n"

    myfile.write(result)
print(f"Data stored in file {filename}")

"""
from datetime import datetime, timedelta
 
week = timedelta(days=7)
 
def format(aika):
    return aika.strftime("%d.%m.%Y")
 
file = input("Filename: ")
start = input("Starting date: ").split('.')
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
 
screen_times = []
total = 0
start = datetime(int(start[2]), int(start[1]), int(start[0]))
 
for i in range(days):
    day = start + timedelta(days=i)
    times = input(f"Screen time {format(day)}: ").split(' ')
    tv = int(times[0])
    pc = int(times[1])
    mobile = int(times[2])
    total += tv + pc + mobile
    screen_times.append((day, tv, pc, mobile) )
 
with open(file, "w") as tdsto:
    tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
    tdsto.write(f"Total minutes: {total}\n")
    tdsto.write(f"Average minutes: {total/days:.1f}\n")
    for pv, tv, pc, mob in screen_times:
        tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")
 
print(f"Data stored in file {file}")
"""
