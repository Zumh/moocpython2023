# Write your solution here:
from random import choice
def word_generator(characters: str, length: int, amount: int):

    # generate random character index including between 0 and len(characters)-1.
    # then combine all together just to make a word and length of amount
    # then return that using yield or dictionary 

    list_of_rand_words = (''.join(choice(characters) for i in range(length)) for i in range(amount))
    return list_of_rand_words
if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)