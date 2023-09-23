# Write your solution here
def add_student(students:dict, name: str):
    students[name] = {}

def print_student(students:dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
    elif students[name] == {}:
        print(f"{name}:\n no completed courses")
    else:
        total_courses = len(students[name])
        print(f"{name}:\n {total_courses} completed courses:")
        grade_total = 0
        for course_name, mark in students[name].items():

            print(f"  {course_name} {mark[1]}")
            grade_total += mark[1]
        average_grade = grade_total/total_courses
        print(f" average grade {average_grade}")
        
def add_course(students:dict, name:str, completed_course:tuple):
    course_name = completed_course[0]
    course_mark = completed_course[1]

    if course_mark > 0:
        # check if the course exist in student data
        if course_name in students[name]:
            # if completed same course's mark are too low then don't bother adding that course
            if course_mark < students[name][course_name][1]:
                return
        # other wise update new course or replace same course with better mark
        students[name][course_name] = completed_course
def summary(students:dict):
    student_count = len(students)
    max_average = {"name":"","average":0.0}
    max_courses = {"name":"", "courses":0}

    grade_total = 0
    for student_name, courses in students.items():
        course_amount = len(courses)
        if max_courses["courses"] < len(courses):
            max_courses["courses"] = len(courses)
            max_courses["name"] = student_name
        
        # calculate the average
        for course_name, course in courses.items():
            grade_total += course[1]
        current_average = grade_total/course_amount
        if max_average["average"] < current_average:
            max_average["average"] = current_average
            max_average["name"] = student_name
        grade_total = 0
        


        
    print(f"students {student_count}")
    print(f"most courses completed {max_courses['courses']} {max_courses['name']}")
    print(f"best average grade {max_average['average']} {max_average['name']}")

