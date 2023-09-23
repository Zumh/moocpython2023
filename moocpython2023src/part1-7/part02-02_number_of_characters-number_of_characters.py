"""
Please write a program which asks the user for a word and then prints out the number of characters, 
if there was more than one typed in.

Examples of expected behaviour:
Please type in a word: hey
There are 3 letters in the word hey
Thank you!

Please type in a word: banana
There are 6 letters in the word banana
Thank you!

Please type in a word: b
Thank you!
"""

word = input("Please type in a word: ")
word_len = len(word)
answer = ""
if word_len > 1 :
    answer = f"There are {word_len} letters in the word {word}\n"
print(answer+"Thank you!")
