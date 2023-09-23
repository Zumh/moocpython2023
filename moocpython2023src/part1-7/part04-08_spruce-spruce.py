
# Write your solution here
def spruce(height):
    space = height - 1
    column = 1
    print("a spruce!")
    while space >= 0:
        # column will be odd number 
        spaces = " " * space
        stars = column * "*"
        print(f"{spaces}{stars}")
        column += 2
        space -= 1 
    print((height - 1) * " " + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)