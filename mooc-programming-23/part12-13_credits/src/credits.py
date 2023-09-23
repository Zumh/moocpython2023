from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list)->int:
    # The function sums up the total number of study credits covered by the courses. 
    return reduce(lambda credit_sum,  student: credit_sum + student.credits, attempts, 0)

def sum_of_passed_credits(attempts: list)->int:
    # The function sums up the credits for the course attempts with grade 1 or above.
    # first we filter passed object from attempt list 
    # then we sum up list of object that are passed
    passed_students = filter(lambda student: student.grade > 0, attempts)
   
    # passed_students is iterative objects
    return reduce(lambda sum_passed_credit, student: sum_passed_credit + student.credits, passed_students, 0)

def average(attempts: list)->float:
    """
    The function calculates the average grade for the course attempts with grade 1 or above.
    """
    # find students with grade 1 or above using filter 
    passed_students = list(filter(lambda student: student.grade >= 1, attempts))
    amount_passed = len(passed_students)
    # here reduce and calculate the summation of grades or call function from above 
    sums_of_grades = reduce(lambda sums_of_grades, student: sums_of_grades + student.grade, passed_students, 0)
    return sums_of_grades / amount_passed
if __name__ == "__main__":
    # Part 1 credit sum | Part 2 The sum of passed credits
    # s1 = CourseAttempt("Introduction to Programming", 5, 5)
    # s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    # s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    # credit_sum = sum_of_all_credits([s1, s2, s3])
    # print(credit_sum)

    # Part 2 The sum of passed credits
    # s1 = CourseAttempt("Introduction to Programming", 5, 5)
    # s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    # s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    # credit_sum = sum_of_passed_credits([s1, s2, s3])
    # print(credit_sum)

    # Part 3 Average grade for passed courses 
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)