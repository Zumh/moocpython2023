# Copy here code of line function from previous exercise

def line(number, a_string):
    if a_string == "":
        print("*"*number)
    else:
        print(a_string[0]*number)

def triangle(size):
    # You should call function line here with proper parameters
    height = 0
    while height <= size:
        line(height, "#")
        height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
