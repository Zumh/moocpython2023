# Write your solution here
def times_ten(start_index: int, end_index: int):
    dict_numbers = {}
    for key in range(start_index, end_index+1):
        dict_numbers[key] = key * 10

    return dict_numbers