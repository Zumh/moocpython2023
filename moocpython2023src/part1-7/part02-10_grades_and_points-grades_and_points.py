"""
The table below outlines the grade boundaries on a certain university course. 
Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.
"""


grade = int(input("How many points [0-100]: "))

message = "impossible!"

if 0 <= grade <= 49:
    message = "fail"
elif 50 <= grade <= 59:
    message = "1"
elif 60 <= grade <= 69:
    message = "2"
elif 70 <= grade <= 79:
    message = "3"
elif 80 <= grade <= 89:
    message = "4"
elif 90 <= grade <= 100:
    message = "5"
print(f"Grade: {message}")