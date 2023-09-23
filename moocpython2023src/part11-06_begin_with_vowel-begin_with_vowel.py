# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(word_list: list)->list:
    return [a_string for a_string in word_list if a_string[0].lower() in "aeiou"]
if __name__ == "__main__":
    word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)