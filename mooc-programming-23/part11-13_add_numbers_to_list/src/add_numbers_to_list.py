# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
    """
    The function takes a list of numbers as its argument, and adds new numbers to the list until the length of the list is divisible by five. 
    Each number added to the list should be one greater than the last number in the list.
    """
    if len(numbers) % 5 != 0:
        # change the internal valaue first 
        numbers.append(numbers[-1]+1)

        # then re-enter the numbers
        add_numbers_to_list(numbers)

if __name__ == "__main__":
    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)