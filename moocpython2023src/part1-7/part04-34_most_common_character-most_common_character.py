# Write your solution here
def most_common_character(a_string:str)->str:

    max_freq = 0
    max_freq_char = ""
    for char in a_string:
        current_freq = a_string.count(char) - 1
        if current_freq > max_freq:
            max_freq = current_freq
            max_freq_char = char 
    return max_freq_char

if __name__ == '__main__':
    """
    clever
    def most_common_character(my_string: str):
    most_common = my_string[0]
    for character in my_string:
        if my_string.count(character) > my_string.count(most_common):
            most_common = character
 
    return most_common
    """