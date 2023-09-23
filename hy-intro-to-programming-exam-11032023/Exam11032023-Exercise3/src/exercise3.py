# Write your solution to exercise 3 here

def convert(my_list, my_function):
    money_convert = []
    for money in my_list:
        money_convert.append(my_function(money))
    return money_convert

def to_euro(number):
    return f'{number} €'

my_list = [2,3,4]

euros = convert(my_list, to_euro)
print(euros) # Prints out: ['2 €', '3 €', '4 €']