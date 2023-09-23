# Write your solution here

import urllib.request
import json

def retrieve_all()->list[tuple]:
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    student_data = my_request.read()
    refine_data = []
    #  part 1
    for data in json.loads(student_data):
        if data["enabled"]:
            refine_data.append((data["fullName"],data["name"],data["year"],sum(data["exercises"])))
    return refine_data

# part 2

def retrieve_course(course_name: str)->dict:
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    student_data = json.loads(my_request.read())
    statistics = {}

    max_students = 0
    total_hours = 0
    exercise_total = 0


    for week in student_data:

        max_students = max(max_students, student_data[week]['students'])
        total_hours += student_data[week]['hour_total']
        exercise_total += student_data[week]['exercise_total']

    #weeks: the number of JSON object literals retrieved
    statistics['weeks'] = len(student_data)
    #students: the maximum number of students in all the weeks
    statistics['students'] = max_students
    #hours: the sum of all hour_total values in the different weeks
    statistics['hours'] = total_hours
    #hours_average: the hours value divided by the students value (rounded down to the closest integer value)
    statistics['hours_average'] = total_hours // max_students
    
    #exercises: the sum of all exercise_total values in the different weeks
    statistics['exercises'] = exercise_total
    
    # exercises_average: the exercises value divided by the students value (rounded down to the closest integer value)
    statistics['exercises_average'] = exercise_total // max_students
    return statistics

    