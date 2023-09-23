"""
Python comparison operators can also be used on strings. 
String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if
the b characters compared are of the same case, i.e. both UPPERCASE or both lowercase
only the standard English alphabet of a to z, or A to Z, is used.
Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Some examples of expected behaviour:

Please type in the 1st word: car
Please type in the 2nd word: scooter
scooter comes alphabetically last.

"""

first_word = input("Pelase type in the 1st word: ")
second_word = input("Please type in the 2nd word: ")
message = "You gave the same word twice."
if first_word != second_word:
    if second_word > first_word:
        first_word = second_word
    message = first_word + " comes alphabetically last."

print(message)