# Write your solution here

from random import choice, sample
def words(n: int, beginning: str):
    # open file and prepare words in a list
    starting_words = []
    random_words = []
    with open("words.txt") as word_list:
        # find word start with beginning
        # if there is none starting word then raise value error
        for word in word_list:
            word = word.strip()
            if word.startswith(beginning):
                starting_words.append(word)
    if len(starting_words) < n:
        raise ValueError("We can not find a single word that match given beginning word")

    # then find the randomize word from the list     
    # make sure word doesn't appear twice
    while len(random_words) < n:
        word = choice(starting_words)

        if  word not in random_words:
            random_words.append(word)

    return(random_words)


    """
    def words(n: int, beginning: str):
    word_list = []
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n","")
            if word.startswith(beginning):
                word_list.append(word)
    if len(word_list) < n:
        raise ValueError("Not enough suitable words can be found!")
    return random.sample(word_list, n)
    """

