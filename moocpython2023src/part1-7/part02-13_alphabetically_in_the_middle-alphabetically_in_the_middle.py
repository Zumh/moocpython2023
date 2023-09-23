"""
Please write a program which asks the user for three letters. 
The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
You may assume the letters will be either all uppercase, or all lowercase.

1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p


"""

first_letter = input("1st letter: ")

second_letter = input("2nd letter: ")

third_letter = input("3rd letter: ")

message = "The letter in the middle is "

if (first_letter < second_letter < third_letter) or (third_letter < second_letter < first_letter):
    message += second_letter
elif (second_letter < first_letter < third_letter) or (third_letter < first_letter < second_letter):
    message += first_letter
else:
    message += third_letter

print(message)
