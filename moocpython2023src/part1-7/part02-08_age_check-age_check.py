
"""
Please write a program which asks for the user's age. 
If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.
What is your age? 13
Ok, you're 13 years old
"""

age = int(input("What is your age? "))
final_message = f"That must be a mistake"

if 0 <= age < 5:
    final_message = "I suspect you can't write quite yet..."
elif age >= 5:
    final_message = f"Ok, you're {age} years old"
print(final_message)