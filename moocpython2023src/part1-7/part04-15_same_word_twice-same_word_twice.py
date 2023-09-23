# Write your solution here
word = ""
words = []
keep_typing = False
while keep_typing == False:
    word = input("Word: ") 
    if word in words:
        keep_typing = True
    else:
        words.append(word) 
print(f"You typed in {len(words)} different words")
