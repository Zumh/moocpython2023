# Write your solution here

import json 
def print_persons(filename: str):
    with open(filename) as myfile:
        data = myfile.read()
    for student_info in json.loads(data):
        print(f"{student_info['name']} {student_info['age']} years ({', '.join(student_info['hobbies'])})")



    