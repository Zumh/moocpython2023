# WRITE YOUR SOLUTION HERE:
from string import punctuation, ascii_letters
def most_common_words(filename: str, lower_limit: int):
    with open(filename, 'r') as my_file:

        words = [word.strip(punctuation) for word in my_file.read().split()]
        return {word:words.count(word) for word in words if words.count(word) >= lower_limit}
if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))