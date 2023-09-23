# Write your solution here
def formatted(my_list:list[float])->list[float]:
    new_list = []

    for num in my_list:
        new_list.append(f"{num:.2f}")
    return new_list