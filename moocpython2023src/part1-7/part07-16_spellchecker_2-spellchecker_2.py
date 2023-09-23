# Write your solution here
import difflib
word_list = []
suggest_words = []
highlighted = ""
with open("wordlist.txt") as myfile:

    for word in myfile:
        word_list.append(word.strip())
input_word = input("write text: ").split(" ")

for word in input_word:
    if word.lower() not in word_list:
        suggest_words.append(f"{word}: {', '.join(difflib.get_close_matches(word, word_list))}")
        word = f"*{word}*"
    
    highlighted += word + " "
print(highlighted)
print("Suggestions:")
for suggest in suggest_words:
    print(f"{suggest}") 