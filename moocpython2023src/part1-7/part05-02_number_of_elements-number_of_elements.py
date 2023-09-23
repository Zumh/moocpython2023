# Write your solution here
def count_matching_elements(my_matrix:list[list[int]], element:int)->int:

    freq_element = 0

    for num_list in my_matrix:

        freq_element += num_list.count(element)

    return freq_element

