"""
Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

Sample output
Please type in a number: 5
1
5
2
4
3

Sample output
Please type in a number: 6
1
6
2
5
3
4
"""
# Write your solution here
high_value = int(input("Please type in a number: "))
low_value = 1

while low_value < high_value:
    print(low_value)
    print(high_value)
    low_value += 1
    high_value -= 1
if high_value == low_value:
    print(low_value)