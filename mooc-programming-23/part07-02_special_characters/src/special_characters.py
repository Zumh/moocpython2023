# Write your solution here

def separate_characters(my_string: str)->tuple:
    from string import punctuation, ascii_letters
    result = tuple
    alphabets = ""
    punctuations = ""
    other_characters = ""
    for char in my_string:
        if char in ascii_letters:
            alphabets += char
        elif char in punctuation:
            punctuations += char
        else: 
            other_characters += char

    result = (alphabets, punctuations, other_characters)
    return result
