# Write your solution here

def length_of_longest(my_list:list[str])->int:
    max_len = 0
    for a_string in my_list:
        current_len = len(a_string)
        if current_len > max_len:
            max_len = current_len
    return max_len

def all_the_longest(my_string:list[str])->list[str]:
    longest_string = []
    max_len = length_of_longest(my_string)
    for string in my_string:
        if len(string) == max_len:
            longest_string.append(string)
    return longest_string
if __name__ == "__main__":
    """
    #Clever solution
    def length_of_longest(names: list):
        longest = 0
    
        for name in names:
            if len(name) > longest:
            longest = len(name)
    
        return longest
    # Write your solution here
    """