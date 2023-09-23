# write your solution here

if False:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
students = {}
exercises = {}
with open(student_info) as student_data:
    for student in student_data:
        student = student.split(";")
        if student[0] != "id":
            students[int(student[0])] = student[1].strip() + " " + student[2].strip()
with open(exercise_data) as exercise_data:
    for exercise in exercise_data:
        exercise = exercise.split(";")                                                 
        if exercise[0] != "id":
            # convert to list of integer
            for indx in range(len(exercise)):
                exercise[indx] = int(exercise[indx])
            # assigned unique id with list of exercises
            exercises[int(exercise[0])]=exercise[1:]
# print student name and completed exercises
for id, name in students.items():
    print(f"{name} {sum(exercises[id])}")