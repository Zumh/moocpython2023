# Write your solution here
def transpose(matrix: list[list[int]]):

    temp_value = 0
    
    for row_indx in range(len(matrix)):
        
        for column_indx in range(row_indx, len(matrix)):

            temp_value = matrix[row_indx][column_indx]
            matrix[row_indx][column_indx] = matrix[column_indx][row_indx]
            matrix[column_indx][row_indx] = temp_value


