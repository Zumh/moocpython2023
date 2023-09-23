# Write your solution to exercise 1 here
numbers = []
user_input = ""
while user_input != '0' : 
    user_input = input("Type in a number: ")
    if user_input != '0' and user_input != "":
        numbers.append(int(user_input))

def find_max(first_num, second_num):
    # function for finding max number
    if first_num <= second_num:
        first_num = second_num
    return first_num

def find_min(first_num, second_num):
    # function for finding min number
    if first_num >= second_num:
        first_num = second_num
    return first_num


unique_number = {}
min_number, max_number = 1, -1
total_sum, count_length = 0, 0
for number in numbers:
    if number not in unique_number:
        unique_number[number] = 0
    unique_number[number] += 1

    max_number = find_max(max_number, number)
    min_number = find_min(min_number, number)
    count_length += 1

    total_sum += number

# find most repeated number
repeated_number = 0
freq = 0
current_freq = 0
for key, value in unique_number.items():

    current_freq = max(current_freq, value)
    if freq < current_freq:
        freq = current_freq
        repeated_number = key 


print(f"Biggest: {max_number}")
print(f"Smallest: {min_number}")
print(f"Number of numbers: {count_length}")
print(f"Sum: {total_sum}")
print(f"Most repeated: {repeated_number}")

