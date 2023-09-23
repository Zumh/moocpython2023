"""
Please write a new version of the program in the previous exercise. 
In addition to the result it should also print out the calculation performed:
assume limit is 2 or higher
Limit: 2
The consecutive sum: 1 + 2 = 3
"""

limit = 0
count_limit = 0

# assuming always start from 1
answer = "1"
total_sum = 0
limit = int(input("Limit: "))
while total_sum < limit:
    total_sum += count_limit
    if count_limit > 1:
        answer += f" + {count_limit}"
    count_limit += 1

print(f"The consecutive sum: {answer} = {total_sum}")