# Write your solution here

def length_of_longest(my_list:list[str])->int:
    max_len = 0
    for a_string in my_list:
        current_len = len(a_string)
        if current_len > max_len:
            max_len = current_len
    return max_len