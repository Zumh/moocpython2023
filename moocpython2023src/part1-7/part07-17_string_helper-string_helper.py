# Write your solution here

def change_case(orig_string: str)->str:
    """
    The function change_case(orig_string: str) creates and returns a new version of the parameter string. 
    The lowercase letters in the original should be uppercase, and uppercase letters should be lowercase.
    """
    change_string = ""
    for letter in orig_string:

        if letter.islower():
            change_string += letter.upper()
        else:
            change_string += letter.lower()
    return change_string

def split_in_half(orig_string: str)->tuple:
    """
    The function split_in_half(orig_string: str) 
    splits the parameter string in half, 
    and returns the results in a tuple. 
    If the original has an odd number of characters, 
    the first half should be shorter.
    """
    # decide odd if the length is odd value 
    string_length = len(orig_string)

    first_half = ""
    second_half = ""
    string_len = string_length//2

    first_half = orig_string[:string_len]
    second_half = orig_string[string_len:]
    return (first_half, second_half)

import string
def remove_special_characters(orig_string: str)->str:
    """
    The function remove_special_characters(orig_string: str) returns a new version of the parameter string, with all special characters removed. 
    Only lowercase and uppercase letters, numbers and spaces are allowed in the returned string.
    """
    new_string = ""
    for letter in orig_string:
        if letter in string.printable and letter not in string.punctuation:
         new_string += letter
    return new_string


