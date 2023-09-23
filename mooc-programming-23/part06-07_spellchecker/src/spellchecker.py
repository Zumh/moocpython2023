# write your solution here

def get_correct_words(file_name):
    correct_words = []
    with open(file_name) as words:

        for word in words:
            correct_words.append(word.strip().lower())
    return correct_words

def main():
    user_input = input("Write text: ").split()
    highlighted_input = ""
    #user_input = "We use ptython to make a spell checker".split()

    correct_words = get_correct_words("wordlist.txt")


    for word in user_input:

        if (word.lower() in correct_words) == False:
            word = f"*{word}*"
        highlighted_input += word + " "
    print(highlighted_input)

main()


