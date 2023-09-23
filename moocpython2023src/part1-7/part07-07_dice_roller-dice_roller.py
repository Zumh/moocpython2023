# Write your solution here

from random import choice
def roll(die: str)->int:
    die_A = [3, 3, 3, 3, 3, 6]
    die_B = [2, 2, 2, 5, 5, 5]
    die_C = [1, 4, 4, 4, 4, 4]
    random_number = 0
    if "A" == die:
        random_number = choice(die_A)
    elif "B" == die:
        random_number = choice(die_B)
    elif "C" == die:
        random_number = choice(die_C)
    
    return random_number
def play(die1: str, die2: str, times: int)->int:
    die1_win = 0
    die2_win = 0
    ties = 0
    result = tuple

    
    for i in range(times):
        track_die1 = roll(die1)
        track_die2 = roll(die2)
        if track_die1>track_die2:
            die1_win += 1
        elif track_die2>track_die1:
            die2_win += 1
        else:
            ties += 1
        
    result = (die1_win,die2_win,ties)

    return result

"""
# smart solution
from random import sample
def roll(die: str):
    dices = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
 
    return sample(dices[die], 1)[0]
 
def play(die1: str, die2: str, times: int):
    v1 = 0
    v2 = 0
    t = 0
    for i in range(times):
        n1 = roll(die1)
        n2 = roll(die2)
        if n1>n2:
            v1 += 1
        elif n1<n2:
            v2 += 1
        else:
            t += 1
    return v1, v2, t
 
"""