# Write your solution here

def no_vowels(my_string:str)->str:
    vowels = "aeiou"
    no_vowel = ""
    for char in my_string:
        if char not in vowels:
            no_vowel += char
    return no_vowel