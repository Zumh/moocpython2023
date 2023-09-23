
# Write your solution here
def hash_square(hash_num):
    each_hash = 0
    while each_hash < hash_num:
        print("#"*hash_num)
        each_hash += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)


    """
    Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.

    hash_square(3)
    print()
    hash_square(5)
    Sample output
    ###
    ###
    ###

    #####
    #####
    #####
    #####
    #####
    """
