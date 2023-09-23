# Write your solution to exercise 2 here

def separate_list(numbers: list[int])->tuple:
    # one in positive and other in negative
    positive_value = []
    negaive_value = []
    # must be in original order
    # wrap two list with tuple 
    for number in numbers:
        if number > 0:
            positive_value.append(number)
        else:
            negaive_value.append(number)
    return positive_value, negaive_value
numbers = [1, -1, 2, -3, 5, -1, 1, 1, 9]
numbers1, numbers2 = separate_list(numbers)
print(numbers1)
print(numbers2)