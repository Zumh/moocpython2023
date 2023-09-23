# Write your solution here

def lottery_numbers(amount: int, lower: int, upper: int)->list:
    from random import sample
    random_numbers = sorted(sample(list(range(lower,upper+1)),amount))

    return random_numbers   

"""
def loterry_numbers(amount: int, lower: int, upper: int)->list:
    from random import randint
    random_numbers = []

    while len(random_numbers) < amount:

        current_rand = randint(lower, upper)

        if current_rand not in random_numbers:
            random_numbers.append(current_rand)
    return sorted(random_numbers)
print(loterry_numbers(3,1,5))
"""