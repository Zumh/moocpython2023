
# Write your solution here
def chessboard(board_length):
    row = 0
    column = 0
    row_num = column_num = 1
    while row < board_length:
        # alternate columns
        while column < board_length:
            print(column_num,end="")
            if column_num == 1:
                column_num = 0
            else:
                column_num = 1

            column += 1
        print()
        column = 0

        # alternate row num 
        if row_num == 1:
            row_num = 0
        else:
            row_num = 1
        # update column num 
        column_num = row_num
        row += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
    print()
    chessboard(6)

    """
    Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes.
    The function takes an integer argument, which specifies the length of the side of the board. 
    See the examples below for details:

    chessboard(3)
    print()
    chessboard(6)
    Sample output
    101
    010
    101

    101010
    010101
    101010
    010101
    101010
    010101
    """

