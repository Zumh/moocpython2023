# Copy here code of line function from previous exercise

def line(number, a_string):
    if a_string == "":
        print("*"*number)
    else:
        print(a_string[0]*number)

def square(size, character):
    # You should call function line here with proper parameters
    row = 0
    while row < size:
        line(size, character)
        row += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")