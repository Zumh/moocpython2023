# Write your solution here
def column_correct(sudoku: list, column_no: int):
    valid_soduku = True 
    number = 1
    freq_column_num = []
    for row in sudoku:    
        number = row[column_no]
        if number > 0 and number in freq_column_num:
            valid_soduku = False
            break
        else:
            freq_column_num.append(number)
    return valid_soduku