"""
Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. 
If the strings are of equal length, the program should print out "The strings are equally long".

Some examples of expected behaviour:
Please type in string 1: hey
Please type in string 2: hiya
hiya is longer
"""

string_1 = input("Please type in string 1: ")
string_2 = input("Please type in string 2: ")
message  = "The strings are equally long"
# if string 2 is longer switch string1 with string2
if len(string_1) > len(string_2):
    message = f"{string_1} is longer"
elif len(string_1) < len(string_2):
    message = f"{string_2} is longer"
print(message)