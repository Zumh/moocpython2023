# Write your solution here
"""
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: auto
The word in English: car
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: roska
The word in English: garbage
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 1
The word in Finnish: laukku
The word in English: bag
Dictionary entry added
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: bag
roska - garbage
laukku - bag
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: car
auto - car
1 - Add word, 2 - Search, 3 - Quit
Function: 2
Search term: laukku
laukku - bag
1 - Add word, 2 - Search, 3 - Quit
Function: 3
Bye!
"""

def print_words(found_words:list):
    
    for word in found_words:
        print(word,end="")
def search_words(dictionary, search_term):
    found_meaning = []
    for words in dictionary:
        if search_term in words:
            found_meaning.append(words)
    return found_meaning

def add_content(meaning:str, file_name:str):
    with open(file_name, "a") as myfile:
        myfile.write(meaning)
with open("dictionary.txt") as file_read, open("dictionary.txt","a") as file_write:
    dictionary = []
    # load the data in a dictionary
    for meaning in file_read:
        dictionary.append(meaning)

    commands = 0
    while commands != 3:
        print("1 - Add word, 2 - Search, 3 - Quit")
        commands = int(input("Function: "))
        if commands == 1:
            finnish = input("The word in Finnish: ")
            english = input("The word in English: ")
            format_meaning = f"{finnish} - {english}\n"
            dictionary.append(format_meaning)
            add_content(format_meaning, "dictionary.txt")
            print("Dictionary entry added")
        elif commands == 2:
            search_term = input("Search term: ")
            # search words 
            found_words = search_words(dictionary, search_term)
            print_words(found_words)

        elif commands == 3:
            print("Bye!")

        
