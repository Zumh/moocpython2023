"""
Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

An example of expected behaviour:

Sample output
Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w
"""


a_string = input("Please type in a sentence: ")
space_index = 0
while space_index >= 0:
    space_index = a_string.find(" ") 
    print(a_string[0])
    if space_index > 0 :
        a_string = a_string[space_index+1:]
