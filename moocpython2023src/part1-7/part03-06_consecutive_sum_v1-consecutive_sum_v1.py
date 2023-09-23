"""
Please write a program which asks the user to type in a limit. 
The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. The program should function as follows:
Limit: 18
21
"""

limit = int(input("Limit: "))
total_sum = 0
count_limit = 0
while total_sum < limit:
    total_sum += count_limit
    count_limit += 1
print(total_sum)