# Write your solution here
def row_correct(sudoku: list, row_no: int):
    valid_soduku = True 
    number = 1
    while number <= 9 and valid_soduku == True:
        if sudoku[row_no].count(number) >= 2:
            valid_soduku = False
        number += 1
    return valid_soduku
            
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

def block_correct(sudoku: list, row_no: int, column_no: int)->bool:
    # check duplicate for row 
    # 1-9
    valid_soduku = True 
    freq_number = []
    for row_indx in range(row_no, row_no + 3):
        for column_indx in range(column_no, column_no + 3):
            number = sudoku[row_indx][column_indx] 
            if number > 0 and number in freq_number:
                valid_soduku = False
                break
            else:
                freq_number.append(number)
    return valid_soduku 

def sudoku_grid_correct(sudoku: list[int]):
    
    blocks = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for block in blocks:
        row_no = block[0]
        column_no = block[1]
        block_check = block_correct(sudoku, row_no, column_no)
        if block_check == False:
            return False
    
    for row_no in range(9):
        
        row_check = row_correct(sudoku, row_no)
        if row_check == False:
            return False 

        for column_no in range(9):
            column_check = column_correct(sudoku, column_no)

            if column_check == False:
                return False    
    return True