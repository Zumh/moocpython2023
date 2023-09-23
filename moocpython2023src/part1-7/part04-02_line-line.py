# Write your solution here

def line(number, a_string):
    if a_string == "":
        print("*"*number)
    else:
        print(a_string[0]*number)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")