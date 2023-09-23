# Write your solution here

"""
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    while beginning <= maximum:
        yield beginning
        beginning += 2
"""
def even_numbers(beginning: int, maximum: int):

    while beginning <= maximum:
        if beginning % 2 == 0:
            yield beginning
        beginning += 1



    
if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)