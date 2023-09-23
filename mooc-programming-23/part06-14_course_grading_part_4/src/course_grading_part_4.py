# tee ratkaisu tänne

def get_exam_data(exam_data:list)->dict:
    exam_points = {}

    for exam in exam_data:
        exam = exam.split(";")
        if exam[0] != "id":
            # convert to list of integer
            
            for indx in range(len(exam)):
                exam[indx] = int(exam[indx])
            exam_points[exam[0]] = exam[1:]
    return exam_points

def get_exercise_data(exercise_data:list)->dict:
    exercises = {}

    for exercise in exercise_data:
        exercise = exercise.split(";")                                                 
        if exercise[0] != "id":
            # convert to list of integer
            for indx in range(len(exercise)):
                exercise[indx] = int(exercise[indx])
            # assigned unique id with list of exercises
            exercises[exercise[0]]=exercise[1:]
    return exercises

def get_exercise_points(completed_exercise:dict)->dict:
    
    exercise_points = {}
    
    for id, exercise in completed_exercise.items():
        exercise_points[id] = sum(exercise) // 4

    return exercise_points

def get_grade(point:int)->int:
    found_grade = 0
    grade_range = [[0,14,0],[15,17,1],[18,20,2],[21,23,3],[24,27,4]]
    if point >= 28:
        found_grade = 5
    else:
        for grade in grade_range:
            if grade[0] <= point <= grade[1]:
                found_grade = grade[2]
                break
        
    return found_grade

def get_student_data(student_info:list)->dict:
    students = {}

    for student in student_info:
        student = student.split(";")
        if student[0] != "id":
            students[int(student[0])] = student[1].strip() + " " + student[2].strip()
    return students


def calculate_statistics(student_info:dict, exercise_data:dict, exercise_points:dict, exam_points:dict):
    satistics = {}
    # print student name and completed exercises
    for id, name in student_info.items():
        sum_of_exampoints = sum(exam_points[id])
        # get point from each exam and exercise
        point = sum_of_exampoints + exercise_points[id]
        # find grade 
        grade = get_grade(point)
        sum_of_exercise = sum(exercise_data[id])
        satistics[id]=[name, sum_of_exercise, exercise_points[id], sum_of_exampoints, point, grade]
    return satistics


def format_output(statistics:dict, title:str, name_width:int, title_width:int):

    underline = "=" * len(title)
    header = f"{'name':{name_width}}{'exec_nbr':{title_width}}{'exec_pts.':{title_width}}{'exm_pts.':{title_width}}{'tot_pts.':{title_width}}{'grade':{title_width}}"
    output_txt = f"{title}\n{underline}\n{header}\n"

    output_csv = ""

    for id, stat in statistics.items():
        output_txt += f"{stat[0]:{name_width}}"
        output_csv += f"{id};{stat[0]};{stat[-1]}\n"
        for number in stat[1:]:
            output_txt += f"{number:<{title_width}}"
        output_txt += "\n"

    return output_txt, output_csv

def get_course_info(course_info):
    title = []
    for info in course_info:
        info = info.split(":")
        title.append(info[1].strip())

    return f"{title[0]}, {title[1]} credits"

# The program start from here 
if False:
    student_information = "students1.csv"
    exercise_completed = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_information = "course3.txt"
else:
    student_information = input("Student information: ")
    exercise_completed = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_information = input("Course information: ")

with open(student_information) as student_info, open(exercise_completed) as exer_completed, open(exam_points) as ex_point, open(course_information) as course_info:
    course_title = get_course_info(course_info)
    student_info = get_student_data(student_info)
    exercise_data = get_exercise_data(exer_completed)
    exercise_points = get_exercise_points(exercise_data)
    exam_points = get_exam_data(ex_point)

statistics = calculate_statistics(student_info, exercise_data, exercise_points, exam_points)
output_txt, output_csv = format_output(statistics,course_title, 30, 10)

txt_file = "results.txt"
csv_file = "results.csv"
with open(txt_file,"w") as txt, open(csv_file,"w") as csv:
    txt.write(output_txt)
    csv.write(output_csv)
