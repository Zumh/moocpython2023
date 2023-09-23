"""
Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in zero.
"""
# Write your solution here
number = None
number_counter = 0
negative_counter = 0
positive_counter = 0
sum_of_number = 0
print("Please type in integer numbers. Type in 0 to finish.")
while (number := int(input("Number: "))) != 0:
    if number < 0:
        negative_counter += 1
    elif number > 0:
        positive_counter += 1
    number_counter += 1
    sum_of_number += number
mean_of_number = sum_of_number/number_counter
print(f"Numbers typed in {number_counter}\n\
The sum of the numbers is {sum_of_number}\n\
The mean of the numbers is {mean_of_number}\n\
Positive numbers {positive_counter}\n\
Negative numbers {negative_counter}")

