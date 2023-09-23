# write your solution here
def largest():
    max_number = 0
    with open("numbers.txt") as numbers:

        for number in numbers:
            current_number = int(number)
            if max_number < current_number:
                max_number = current_number
    return(max_number)

