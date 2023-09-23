# Write your solution here
def remove_smallest(numbers: list[int]):
    smallest_number = numbers[0]
    # find the smallest number in a list 
    for number in numbers:
        if smallest_number > number:
            smallest_number = number
    # then remove that number from the list
    numbers.remove(smallest_number)