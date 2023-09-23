
# write your solution here
def get_student_data(student_info):
    students = {}
    with open(student_info) as student_data:
        for student in student_data:
            student = student.split(";")
            if student[0] != "id":
                students[int(student[0])] = student[1].strip() + " " + student[2].strip()
    return students

def get_exercise_data(exercise_data):
    exercises = {}
    with open(exercise_data) as exercise_data:
        for exercise in exercise_data:
            exercise = exercise.split(";")                                                 
            if exercise[0] != "id":
                # convert to list of integer
                for indx in range(len(exercise)):
                    exercise[indx] = int(exercise[indx])
                # assigned unique id with list of exercises
                exercises[exercise[0]]=exercise[1:]
    return exercises
def get_exam_data(exam_data):
    exam_points = {}
    with open(exam_data) as exam_data:
        for exam in exam_data:
            exam = exam.split(";")
            if exam[0] != "id":
                # convert to list of integer
                
                for indx in range(len(exam)):
                    exam[indx] = int(exam[indx])
                exam_points[exam[0]] = exam[1:]
    return exam_points
def get_exercise_points(completed_exercise):
    
    exercise_points = {}
    
    for id, exercise in completed_exercise.items():
        exercise_points[id] = sum(exercise) // 4

    return exercise_points
def get_grade(point):
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

def main():
    if False:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_data = input("Exam points: ")
    else:
        # now this is the False branch, and is never executed
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_data = "exam_points1.csv"
    student_data = get_student_data(student_info) 
    completed_exercise = get_exercise_data(exercise_data)
    exam_points = get_exam_data(exam_data)
    
    # get exercise points 
    exercises_points = get_exercise_points(completed_exercise)

    
    name_width = 30
    title_width = 10
    print(f"{'name':{name_width}}{'exec_nbr':{title_width}}{'exec_pts.':{title_width}}{'exm_pts.':{title_width}}{'tot_pts.':{title_width}}{'grade':{title_width}}")
    # print student name and completed exercises
    for id, name in student_data.items():
        sum_of_exampoints = sum(exam_points[id])
        # get point from each exam and exercise
        point = sum_of_exampoints + exercises_points[id]

        # find grade 
        grade = get_grade(point)

        sum_of_exercise = sum(completed_exercise[id])

        print(f"{name:{name_width}}{sum_of_exercise:<{title_width}}{exercises_points[id]:<{title_width}}{sum_of_exampoints:<{title_width}}{point:<{title_width}}{grade:<{title_width}}")
    


main()