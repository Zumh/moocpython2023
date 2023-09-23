# Copy here code of line function from previous exercise and use it in your solution

def line(number, a_string):
    if a_string == "":
        print("*"*number)
    else:
        print(a_string[0]*number)

def shape(height, tri_char, length, rect_char):
    count_height = 0
    # triangle
    while count_height <= height:
        line(count_height, tri_char)
        count_height += 1
    # rectangle 
    count_height = 0
    while count_height < length:
        line(height, rect_char)
        count_height += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")