# Write your solution here

from datetime import datetime, timedelta
import csv

def final_points():
    allow_time = timedelta(hours=3)
    exam_info = {}
    final_point_info = {}
    with open("start_times.csv") as start_times, open("submissions.csv") as submit_times:
        for row in csv.reader(start_times, delimiter=";"):
            student_name = row[0]
            time = datetime.strptime(row[-1],"%H:%M") 
            if student_name not in exam_info:
                exam_info[student_name] = {"start_time":time}
            elif exam_info[student_name]["start_time"] > time:
                exam_info[student_name]["start_time"] = time

        for row in csv.reader(submit_times, delimiter=";"):
            student_name = row[0]
            submit_time = datetime.strptime(row[-1],"%H:%M") 
            points = int(row[-2])
            tasks = row[1]
            
            if 'tasks' not in exam_info[student_name]:
                exam_info[student_name]["tasks"]={}

            if tasks not in exam_info[student_name]['tasks']:
                exam_info[student_name]["tasks"][tasks]=points
            elif abs( submit_time - exam_info[student_name]["start_time"]) <= allow_time and exam_info[student_name]['tasks'][tasks] < points:
                exam_info[student_name]['tasks'][tasks] = points


        for name in exam_info:

            final_point_info[name] = sum(exam_info[name]['tasks'].values())
            
    return final_point_info

