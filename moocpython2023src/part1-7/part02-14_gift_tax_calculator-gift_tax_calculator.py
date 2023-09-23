"""
Please write a program which calculates the correct amount of tax for a gift from a close relative. 
Have a look at the examples below to see what is expected. 
Notice the lack of thousands separators in the input values 
- you may assume there will be no spaces or other thousands separators in the numbers in the input, as we haven't yet covered dealing with these.
"""

# Write your solution here
# get the gift from user input

gift = int(input("Value of gift: "))
answer = f"Amount of tax: "
tax = 0
# gift value ragne from 5000 - 25000
MAX_GIFT = 25000
MIN_GIFT = 5000
TAX_RATE = 8/100
LOWER_LIMIT = 100 
if MIN_GIFT <= gift < MAX_GIFT:
    tax = LOWER_LIMIT + ((gift - MIN_GIFT) * TAX_RATE)
MIN_GIFT = 25000
MAX_GIFT = 55000
TAX_RATE = 10/100
LOWER_LIMIT = 1700

if MIN_GIFT <= gift < MAX_GIFT:
    tax = LOWER_LIMIT + ((gift - MIN_GIFT) * TAX_RATE)

MIN_GIFT = 55000
MAX_GIFT = 200000
TAX_RATE = 12/100
LOWER_LIMIT = 4700
if MIN_GIFT <= gift < MAX_GIFT:
    tax = LOWER_LIMIT + ((gift - MIN_GIFT) * TAX_RATE)

MIN_GIFT = 200000
MAX_GIFT = 1000000
TAX_RATE = 15/100
LOWER_LIMIT = 22100
if MIN_GIFT <= gift < MAX_GIFT:
    tax = LOWER_LIMIT + ((gift - MIN_GIFT) * TAX_RATE)


MIN_GIFT = 1000000
TAX_RATE = 17/100
LOWER_LIMIT = 142100
if MIN_GIFT <= gift :
    tax = LOWER_LIMIT + ((gift - MIN_GIFT) * TAX_RATE)

if tax > 0:
    print(f"Amount of tax: {tax} euros")
else:
    print("No tax!")