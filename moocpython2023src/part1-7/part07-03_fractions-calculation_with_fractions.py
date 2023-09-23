# Write your solution here
def fractionate(amount: int)->list:
    from fractions import Fraction
    list_fractions = []
    for number in range(amount):
        list_fractions.append(Fraction(1,amount))

    return list_fractions
