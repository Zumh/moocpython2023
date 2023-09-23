

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
