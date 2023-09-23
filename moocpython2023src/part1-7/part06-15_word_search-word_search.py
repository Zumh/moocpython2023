# Write your solution here
def asterisk_words(search_term:str, word_list:list)->list:
    found_word = []
    
    
    # check for the word after the asterisk
    if search_term.startswith("*"):
        end_word = search_term[1:]
        for word in word_list:
            if word.endswith(end_word):
                found_word.append(word)
    elif search_term.endswith("*"):
        start_word = search_term[:-1]
        for word in word_list:
            if word.startswith(start_word):
                found_word.append(word)
    
    return found_word
def dot_words(search_term:str, word_list:list)->list:
    # same position and same length

    found_word = []
    is_found = False
    # split the search_term in a list
    for word in word_list:
        if len(word) == len(search_term):
            for search_term_indx in range(len(search_term)):
                char = search_term[search_term_indx]
                # must be same position with search_term and current word
                # except the dot
                if char != ".":
                    if word[search_term_indx] == search_term[search_term_indx]:
                        is_found = True 
                    else:
                        is_found = False
                        break
        # also search term and word must be the same length
        if is_found == True:
            found_word.append(word)
        is_found = False
    return found_word
def find_words(search_term: str):
    word_list = []
    found_list = []
    with open("words.txt") as words:
        for word in words:
            word_list.append(word.strip())
    
    if "*" in search_term:
        # asterisk wild card
        found_list = asterisk_words(search_term, word_list)
    elif "." in search_term:
        # dot wild card
        found_list = dot_words(search_term, word_list)

    else:
        # search the word in word_list 
        # one word search
        for word in word_list:

            if search_term == word:
                found_list.append(word)
    return found_list


