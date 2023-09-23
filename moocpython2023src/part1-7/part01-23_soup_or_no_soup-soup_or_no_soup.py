"""
Please write a program which asks for the user's name. 
If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. 
The price of a single portion is 5.90.

Two examples of the program's execution:

Please tell me your name: Kramer
How many portions of soup? 2
The total cost is 11.8
Next please!

Please tell me your name: Jerry
Next please!
"""

name = input("Please tell me your name: ")
avoid_name = "Jerry"

if name != avoid_name:  
    single_portion_price = 5.90
    soup_portion = int(input("How many portions of soup? "))
    total_cost = soup_portion * single_portion_price
    print(f"The total cost is {total_cost}")
print("Next please!")