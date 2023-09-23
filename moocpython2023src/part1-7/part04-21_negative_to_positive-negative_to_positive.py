# Write your solution here

pos_number = int(input("Please type in a positive integer: "))

for number in range(-pos_number, pos_number+1):
    if number != 0:
        print(number)