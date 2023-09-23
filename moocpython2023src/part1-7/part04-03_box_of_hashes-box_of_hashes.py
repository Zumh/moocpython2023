# Copy here code of line function from previous exercise

def line(number, a_string):
    if a_string == "":
        print("*"*number)
    else:
        print(a_string[0]*number)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    each_height = 0
    while each_height < height:
        line(10, "#")
        each_height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
