# Write your solution here
def first_word(sentence):
    space_indx = sentence.find(" ")
    if space_indx >= 0:
        return sentence[:space_indx]
    else:
        return sentence

def second_word(sentence):
    count_word = 0
    word_len = 0
    word = ""
    while count_word < 2:
        word = first_word(sentence[word_len:])
        word_len += len(word) + 1
        count_word += 1
    return word

def last_word(sentence):

    word_len = 0
    current_word = sentence
    found_word = sentence
    while current_word != "":
        found_word = current_word

        current_word = first_word(sentence[word_len:])
        word_len += len(current_word) + 1

    return found_word
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))