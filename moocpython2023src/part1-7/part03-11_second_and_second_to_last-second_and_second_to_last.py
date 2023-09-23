"""
Please write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a
"""

a_string = input("Please type in a string: ")

second_character = a_string[1]
second_last_character = a_string[-2]
message = f"The second and the second to last characters are "
if second_character == second_last_character:
    message += f"{second_character}"
else:
    message += "different"
print(message)