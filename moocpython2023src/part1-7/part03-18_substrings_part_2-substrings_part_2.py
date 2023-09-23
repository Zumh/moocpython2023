"""
Please write a program which asks the user to type in a string. 
The program then prints out all the substrings which end with the last character, from the shortest to the longest. 
Have a look at the example below.

Sample output
Please type in a string: test
t
st
est
test
"""

word = input("Plese type in a string: ")
index = len(word)-1

while index >= 0:
    print(word[index:])
    index -= 1