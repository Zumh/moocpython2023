"""
Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

Some examples of expected behaviour:

Sample output
Please type in a string: abcabc
Please type in a substring: ab
The second occurrence of the substring is at index 3.

Sample output
Please type in a string: methodology
Please type in a substring: o
The second occurrence of the substring is at index 6.

Sample output
Please type in a string: aybabtu
Please type in a substring: ba
The substring does not occur twice in the string.
"""


a_string = input("Please type in a string: ")

sub_string =  input("Please type in a substring: ")

# find user input character 2nd occurance
# quit if  

occurance_count = 0 
index = 0
found_index = 0
or_len = len(sub_string)


while index < len(a_string) and occurance_count < 2:
    end_dex = or_len + index
    if sub_string == a_string[index:end_dex]:
        occurance_count += 1
        found_index = index
        index = end_dex
    index += 1
    
if occurance_count == 2:
    print(f"The second occurrence of the substring is at index {found_index}.")
else:
    print("The substring does not occur twice in the string.")