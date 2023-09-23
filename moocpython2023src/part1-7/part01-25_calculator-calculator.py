"""
Please write a program which asks the user for two numbers and an operation. 
If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. 
If the user types in anything else, the program should print out nothing.

Some examples of expected behaviour:
Number 1: 10
Number 2: 17
Operation: add/ multiply/ subtract

10 + 17 = 27
"""

number1 = int(input("Number 1: "))

number2 = int(input("Number 2: "))

operation = input("Operation: ")

result = ""

if operation == "add":
    result = f"{number1} + {number2} = {number1 + number2}"
elif operation == "subtract":
    
    result = f"{number1} - {number2} = {number1 - number2}"

elif operation == "multiply":
    
    result = f"{number1} * {number2} = {number1 * number2}"
print(result)