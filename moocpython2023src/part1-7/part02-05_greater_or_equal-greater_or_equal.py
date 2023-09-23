"""
Please write a program which asks for two integer numbers. 
The program should then print out whichever is greater. 
If the numbers are equal, the program should print a different message.

Some examples of expected behaviour:

Please type in the first number: 5
Please type in another number: 3
The greater number was: 5
"""

first_number = int(input("Please type in the first number: "))
second_number = int(input("Please type in another number: "))
message = "The greater number was: "
if first_number > second_number:
    message = f"{message} {first_number}"
elif first_number < second_number:

    message = f"{message} {second_number}"
else: 
    message = "The numbers are equal!"
print(message)