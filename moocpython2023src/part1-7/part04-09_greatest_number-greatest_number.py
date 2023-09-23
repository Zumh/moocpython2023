# Write your solution here
def find_max(first_num, second_num):
    if first_num < second_num:
        first_num = second_num
    return first_num
def greatest_number(first_numb, second_numb, third_numb):
    return find_max(find_max(first_numb, second_numb), third_numb)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)