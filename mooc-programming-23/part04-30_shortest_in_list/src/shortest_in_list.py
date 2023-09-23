# Write your solution here
def shortest(my_list:list[str])->str:
    min_len = 10000
    min_str = ""

    for a_string in my_list:

        current_len = len(a_string)

        if current_len < min_len:
            min_len = current_len
            min_str = a_string

    return min_str
