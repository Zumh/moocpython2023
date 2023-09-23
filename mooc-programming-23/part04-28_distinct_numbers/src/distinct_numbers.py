# Write your solution here
def distinct_numbers(numbers:list[int])->list[int]:

    distinct_list = []

    for number in numbers:
        if number not in distinct_list:
            distinct_list.append(number)

    return sorted(distinct_list)