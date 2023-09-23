"""
Please write a program which asks for the names and ages of two persons. 
The program should then print out the name of the elder.

Some examples of expected behaviour:

Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada
"""
# Write your solution here

older_or_same = "The elder is "

print("Person 1:")
first_person_name = input("Name: ")
first_person_age = int(input("Age: "))

print("Person 2:")
second_person_name = input("Name: ")
second_person_age = int(input("Age: "))

elder_or_same = f"The elder is "
if first_person_age > second_person_age:
    elder_or_same += first_person_name
elif first_person_age < second_person_age:
    elder_or_same += second_person_name
elif second_person_age == first_person_age:
    elder_or_same = f"{first_person_name} and {second_person_name} are the same age" 

print(elder_or_same)