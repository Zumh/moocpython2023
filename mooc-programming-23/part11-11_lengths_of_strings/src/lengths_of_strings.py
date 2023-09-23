# WRITE YOUR SOLUTION HERE:
def lengths(word_list: list)->dict:
    return {word:len(word) for word in word_list}
if __name__ == "__main__":
    word_list = ["once", "upon" , "a", "time", "in"]

    word_lengths = lengths(word_list)
    print(word_lengths)