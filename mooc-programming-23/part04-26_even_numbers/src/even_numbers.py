# Write your solution here

def even_numbers(numbers:list[int])->list[int]:

    even_list = []

    for number in numbers:
        if number%2 == 0:
            even_list.append(number)
    return even_list