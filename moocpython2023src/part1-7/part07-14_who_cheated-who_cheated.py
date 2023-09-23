# Write your solution here

from datetime import datetime, timedelta
def cheaters():
    exam_info = {}

    with open("start_times.csv") as start_time_file, open("submissions.csv") as submit_time_file:
        # convert csv file to json list
        
        for time in start_time_file:
            time = time.strip().split(";")
            student_name = time[0]
            if student_name not in exam_info:
                exam_info[time[0]] = {"start":[time[1]]}
            else:
                exam_info[time[0]]["start"].append(time[1])

        for time in submit_time_file:
            time = time.strip().split(";")
            student_name = time[0]
            if 'submit' not in exam_info[time[0]]:
                exam_info[time[0]]['submit'] = [time[-1]]
            else:
                exam_info[time[0]]["submit"].append(time[-1])


    allow_time = timedelta(hours=3)
    cheater_names = []
    for name in exam_info:
        # convert time and find the difference 
        start = min(exam_info[name]['start'])
        submit = max(exam_info[name]['submit'])
        
        spend_time = abs(datetime.strptime(start,"%H:%M") - datetime.strptime(submit,"%H:%M"))
        print(f"{name:<30}{start} {submit} {spend_time}")
        if spend_time > allow_time:

            cheater_names.append(name)

    return cheater_names
cheaters()
"""
import csv
from datetime import datetime, timedelta
 
def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        # Then read submissions
        # From each student, last (i.e. greatest) is saved
        submission_times = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            # If name does not exists in dictionary, add time directly to the dictionary
            if name not in submission_times:
                submission_times[name] = time
            # If there alredy exists time for key, compare if current time is greater
            elif time > submission_times[name]:
                submission_times[name] = time
        
        cheaters = []
        # Iterate through students one by one
        for name in start_times:
            if submission_times[name] - start_times[name] > timedelta(hours = 3):
                cheaters.append(name)
 
        return cheaters
"""




