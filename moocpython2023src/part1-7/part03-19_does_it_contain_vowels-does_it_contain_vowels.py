"""
Please write a program which asks the user to input a string. 
The program then prints out different messages if the string contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

Sample output
Please type in a string: hello there
a not found
e found
o found

Sample output
Please type in a string: hiya
a found
e not found
o not found
"""

index = 0 
word = input("Please type in a string: ")
find_word = "aeo"
result = ""
while index < len(find_word) :
    result = find_word[index]
    if find_word[index] in word:
        result += " found"
    else:
        result += " not found"
    print(result)
    index += 1


