# Write your solution here
def factorials(n: int)->int:

    factor = 1
    dict_fact = {}
    for key in range(1, n+1):
        factor *=  key
        dict_fact[key] = factor
    return dict_fact


        