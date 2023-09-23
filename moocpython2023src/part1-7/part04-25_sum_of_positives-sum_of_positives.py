# Write your solution here

def sum_of_positives(number:list[int]):
    pos_sum = 0 
    for each_num in number:
        if each_num > 0:
            pos_sum += each_num 
    return pos_sum
