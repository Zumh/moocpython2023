# Write your solution here
def row_correct(sudoku: list, row_no: int):
    valid_soduku = True 
    number = 1
    while number <= 9 and valid_soduku == True:
        if sudoku[row_no].count(number) >= 2:
            valid_soduku = False
        number += 1
    return valid_soduku
            