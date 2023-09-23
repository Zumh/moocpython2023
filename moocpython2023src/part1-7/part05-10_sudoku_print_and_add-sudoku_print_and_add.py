# Write your solution here

def print_sudoku(sudoku:list[list[int]]):
    dashes = ""
    for row_indx in range(9):
        for column_indx in range(9):
            if sudoku[row_indx][column_indx] > 0:
                dashes += str(sudoku[row_indx][column_indx])
            else:
                dashes += "_"
            dashes += " "
            if (column_indx+1) % 3 == 0:
                dashes += " "
        print(f"{dashes}")
        if (row_indx+1) % 3 == 0:
            print()
        dashes = ""
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
