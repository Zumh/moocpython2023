# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int)->list[list[int]]:
    sudoku_copy = []
    for numbers in sudoku:
        sudoku_copy.append(numbers[:])
    sudoku_copy[row_no][column_no] = number 

    return sudoku_copy
