# Write your solution here

def longest_series_of_neighbours(numbers:list[int])->int:

    max_len = 0
    current_len = 0
    different = 0
    for index in range(len(numbers)):
        different = abs(numbers[index-1] - numbers[index])
        if different == 1:
            current_len += 1
        else:
            current_len = 1
        
        if current_len > max_len:
            max_len = current_len

    return max_len