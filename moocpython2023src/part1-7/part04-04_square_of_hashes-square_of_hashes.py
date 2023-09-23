# Copy here code of line function from previous exercise

def line(number, a_string):
    if a_string == "":
        print("*"*number)
    else:
        print(a_string[0]*number)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    count_height = 0
    while count_height < size:
        line(size, "#")
        count_height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
