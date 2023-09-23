
def squared(a_string, number):
    row = 0 
    column = 0
    next_index = 0
    square_string = ""
    while row < number:

        while column < number:
            # switch to the beginning if out of range in string
            if next_index > len(a_string)-1:
                next_index = 0
            square_string += a_string[next_index]
            # go to next character in a string
            next_index += 1

            column += 1
        print(square_string)

        # updating all the variables
        square_string = ""
        column = 0
        row += 1
if __name__ == "__main__":

    squared("ab", 3)
    squared("aybabtu", 5)

    """
    Please write a function named squared, 
    which takes a string argument and an integer argument, 
    and prints out a square of characters as specified by the examples below.

    squared("ab", 3)
    print()
    squared("aybabtu", 5)
    Sample output
    aba
    bab
    aba

    aybab
    tuayb
    abtua
    ybabt
    uayba
    """
