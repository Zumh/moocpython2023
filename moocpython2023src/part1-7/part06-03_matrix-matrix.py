# write your solution here
def get_matrix():
    int_matrix = []
    with open("matrix.txt") as matrix:
        for number in matrix:
            number = number.replace("\n","")
            each_row = number.split(",")
            # convert to integer
            for indx in range(len(each_row)):
                each_row[indx] = int(each_row[indx])
            int_matrix.append(each_row)
    return int_matrix


def matrix_max():
    greatest_value = 0
    matrix = get_matrix()
    for number in matrix:
        greatest_value = max(greatest_value, max(number))
    return(greatest_value)
def row_sums():
    row_sum_list = []
    matrix = get_matrix()
    for number in matrix:
        row_sum_list.append(sum(number))
    return(row_sum_list)



def matrix_sum():
    total_sum = 0
    matrix = get_matrix()
    for number in matrix:
        total_sum += sum(number)
    return(total_sum)