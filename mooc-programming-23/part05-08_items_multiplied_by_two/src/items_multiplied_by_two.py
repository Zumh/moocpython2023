# Write your solution here
def double_items(numbers: list[int])->list[int]:
    double_nums = []

    for number in numbers:
        double_nums.append(number * 2)
    return double_nums