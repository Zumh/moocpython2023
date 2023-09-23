"""
Please change the program from the previous exercise so that the user 
gets to input also the base which is multiplied (in the previous program the base was always 2).
"""

power = int(input("Upper limit: "))
product = 1
base = int(input("Base: "))

while product <= power:
    print(product)
    product *= base