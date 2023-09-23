# Write your solution here


# calculate exercise to points
def completed_exercise_to_points(completed_exercise):
    for indx in range(len(completed_exercise)):
        completed_exercise[indx] = completed_exercise[indx] // 10

# convert exam + exercise points to grade
def get_grade(exam_points, exercise_points):
    grades = []
    given_grades = [[0,14,0],[15,17,1],[18,20,2],[21,23,3],[24,27,4],[28,30,5]]
    for indx in range(len(exam_points)):
        # less than 10 point exam, fail the student, regardless of total number points
        if exam_points[indx] >= 10:
            point = exam_points[indx] + exercise_points[indx]
            for grade in given_grades:
                if grade[0] <= point <=grade[1]:
                    grades.append(grade[2])
                    break
        else:
            grades.append(0)
    return grades
# get input from the user
def get_exercise_exam_points(exam_points, exercise_points):
    points = None
    
    while points != "":
        points = input("Exam points and exercises completed: ")
        if points != "":
            points = points.split(" ")
            # convert to integer 
            exam_points.append(int(points[0]))
            exercise_points.append(int(points[1]))

    
    if len(exercise_points) > 0: 
        # convert exercise completion to points 
        completed_exercise_to_points(exercise_points)

# calculate satistics
def calculate_satistics(exam_points, exercise_points, grades):
    satistics = []
    #calculate points average 
    points_average = (sum(exam_points) + sum(exercise_points)) / len(exam_points)

    satistics.append(points_average)

    #calculate pass percentage 
    count_passing_grade = 0
    for grade in grades:
        if grade > 0:
            count_passing_grade += 1
    pass_percentage = (count_passing_grade/len(grades)) * 100
    satistics.append(pass_percentage)

    return satistics

    
# print statistics 
def print_statistics(satistics, grades):
    point_average, pass_percent = satistics[0],satistics[1]
    print("Statistics:")
    print(f"Points average: {point_average:.1f}\nPass percentage: {pass_percent:.1f}")
    print(f"Grade distribution:\n"
   +"  5: "+grades.count(5)*"*"+"\n"
   +"  4: "+grades.count(4)*"*"+"\n"
   +"  3: "+grades.count(3)*"*"+"\n"
   +"  2: "+grades.count(2)*"*"+"\n"
   +"  1: "+grades.count(1)*"*"+"\n"
   +"  0: "+grades.count(0)*"*")
   
# main function for organizing all the pieces 
def main():
    exam_points = []
    exercise_points = []
    # get user input exam and exercise points 
    get_exercise_exam_points(exam_points, exercise_points)
    
    # get grades
    grades = get_grade(exam_points, exercise_points)

    # calculate the satistic 
    # satiscis = [points_average, pass_percentage]
    satistics = calculate_satistics(exam_points,exercise_points,grades)
    
    # print the satistic 
    print_statistics(satistics, grades)

main()