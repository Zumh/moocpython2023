# tee ratkaisusi tänne

"""
key = courses
{
    course: {
                grade: # replace grade with max
                credit:
            }
}
Pretend this is for one student course completetion info
"""
class Course:
    """
    This course class is for initialization of a course template
    """
    def __init__(self, name: str):
        self.__name = name
        self.__grade = None 
        self.__credit = None
    
    def course(self)->str:
        return self.__name 
    
    def grade(self)->int:
        return self.__grade 
    
    def credit(self)->int:
        return self.__credit 

    def add_grade(self, grade: int):
        self.__grade = grade
    
    def add_credit(self, credit: int):
        self.__credit = credit 
    
class CourseLogic:
    """
    This class will handle the logic of courses and mostly relate to data ins and outs.
    """
    def __init__(self):
        self.__courses = {}
    
    # add courses
    def add_grade(self, name: str, grade: int)->bool:
        if not name in self.__courses:
            self.__courses[name] = Course(name)
        elif self.__courses[name].grade() > grade:
            return False
        self.__courses[name].add_grade(grade)
        return True 
    
    # search course using course name
    def add_cedit(self, name: str, credit: int):
        if not name in self.__courses:
            self.__courses[name] = Course(name)
        self.__courses[name].add_credit(credit)
        
    def add_course(self, name: str, grade: int, credit: int):
        if self.add_grade(name, grade) == True:
            self.add_cedit(name, credit)

    # get one specific course data
    def get_course_data(self, name: str)->Course:
        if not name in self.__courses:
            return None 
        return self.__courses[name]

       
    def calculate_satistics(self):
        course_statistics = {}
        grade_frequency = {}

        completed_courses = len(self.__courses)
        course_statistics['completed_courses'] = completed_courses

        total_grade = 0
        total_credit = 0
        grade_mean = 0
        grade_frequency = {1:0, 2:0, 3:0, 4:0, 5:0}
        for cours_name, course in self.__courses.items():
            grade_frequency[course.grade()] += 1
            total_grade += course.grade()
            total_credit += course.credit()
        grade_mean = total_grade / completed_courses
        course_statistics['grade_mean'] = grade_mean
        course_statistics['total_credit'] = total_credit

        return course_statistics, grade_frequency
    # get_all_entries
    def all_entries(self):
        return self.__courses

class CourseApplication:
    """
    This class will handle the out put format of courses and satistics
    Also satistics will be calculate here 
    """
    def __init__(self):
        self.__courselogic = CourseLogic()
    
    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_courses()
            elif command == "2":
                self.search_course()
            elif command == "3":
                self.get_satistics()
            else:
                self.help()
    
    def add_courses(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__courselogic.add_course(name, grade, credits)

    def search_course(self):
        name = input("name: ")
        data = self.__courselogic.get_course_data(name)

        if data == None:
            print("no entry for this course")
            return

        print(f"{data.course()} ({data.credit()} cr) grade {data.grade()}")

    def get_satistics(self):
        
        course_statistics, grade_frequency  = self.__courselogic.calculate_satistics()
        print(f"{course_statistics['completed_courses']} completed courses, a total of {course_statistics['total_credit']} credits")
        print(f"mean {course_statistics['grade_mean']:.01f}")
        print("grade distribution")
        for grade in range(len(grade_frequency), 0, -1):
            print(f"{grade}: {'x'*grade_frequency[grade]}")


application = CourseApplication()
application.execute()
 

    
 """
 class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name 
        self.__grade = grade
        self.__credits = credits
 
    def grade(self):
        return self.__grade
 
    def credits(self):
        return self.__credits
 
    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
 
class StudyRecords:
    def __init__(self):
       self.courses = {}    
 
    def add_completion(self, course_name, grade, op):
        if course_name in self.courses and self.courses[course_name].grade() > grade:
            return
 
        self.courses[course_name] = Course(course_name, grade, op)
 
    def get_completion(self, course_name):
        if not course_name in self.courses:
            return None
 
        return self.courses[course_name]        
 
    def get_statistics(self):
        number_of_courses = len(self.courses)
        credits = 0
        sum_of_grades = 0
        grades = [0, 0, 0, 0, 0, 0, 0]
 
        for courses in self.courses.values():
            credits += courses.credits()
            sum_of_grades += courses.grade()
            grades[courses.grade()] += 1
        
        return {
            "number_of_courses": number_of_courses,
            "credits": credits,
            "average": sum_of_grades / number_of_courses,
            "grades": grades
        }
 
class Application:
    def __init__(self):
        self.register = StudyRecords()     
 
    def ohje(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
 
    def new_completion(self):
        course_name = input("course: ")
        grade = int(input("grade: "))
        op = int(input("credits: "))
        self.register.add_completion(course_name, grade, op)
 
    def get_completion(self):
        course_name = input("course: ")
        courses = self.register.get_completion(course_name)
        if courses is None:
            print("no entry for this course")
        else:
            print(courses)        
 
    def statistics(self):
        t = self.register.get_statistics() 
 
        print(f"{t['number_of_courses']} completed courses, a total of {t['credits']} credits")
        print(f"mean {t['average']:.1f}")
        print("grade distribution")
        for i in range(5, 0, -1):
            grade_hits = t['grades'][i]
            row = "x"*grade_hits
            print(f"{i}: {row}")        
 
    def execute(self):
        self.ohje()
 
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command=="1":
                self.new_completion()
            elif command=="2":
                self.get_completion()
            elif command=="3":
                self.statistics()
 
Application().execute()
 """

