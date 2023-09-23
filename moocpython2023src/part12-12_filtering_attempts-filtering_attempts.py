class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list)->list[CourseAttempt]:
    """
    The function should return a new list of CourseAttempt objects, 
    including only those items from the original list whose grade is at least 1.
    """
    return list(filter(lambda x:x.grade >= 1, attempts))

def attempts_with_grade(attempts: list, grade: int)->list[CourseAttempt]:
    """
    The function should return a new list containing only those CourseAttempt objects from 
    the original list whose grade matches the second argument.
    """

    return list(filter(lambda x:x.grade == grade, attempts))

def passed_students(attempts: list, course: str)->list[str]:
    """
    The function should return an alphabetically ordered list of names of those students who passed the course, i.e. 
    their grade for the given course was higher than 0.
    """
    return sorted(list(map(lambda student : student.student_name, filter(lambda attempt: attempt.course_name == course and attempt.grade > 0  , attempts))))
if __name__ == "__main__":

    # Part 1 | Part 2 
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)

    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)
    s5 = CourseAttempt("Jack Java", "Introduction to AI", 3)
    s6 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)

    # for attempt in accepted([s1, s2, s3]):
    #     print(attempt)

    # for attempt in attempts_with_grade([s1, s2, s3, s4, s5], 3):
    #     print(attempt)

    for attempt in passed_students([s1, s2, s3, s4, s5, s6], "Introduction to AI"):
        print(attempt)