# Write your solution here
def generate_password(pass_length:int)->str:
    from string import ascii_lowercase
    from random import randint
    password = ""
    while len(password) < pass_length:
        indx = randint(0,25)

        if ascii_lowercase[indx] not in password:
            password += ascii_lowercase[indx]
    return password


"""
from random import choice
from string import ascii_lowercase
 
def generate_password(length: int):
    passwd = ""
    for i in range(length):
        passwd += choice(ascii_lowercase)
 
    return passwd
 
"""