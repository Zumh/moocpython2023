"""
Please write a program which asks the user to type in an upper limit. 
The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. 
That is, the program prints out powers of two in order.

The execution of the program finishes when the next number to be printed would be greater than the limit set by the user. No numbers greater than the limit should be printed.
"""
number = int(input("Upper limit: "))
doubled_number = 1
while doubled_number <= number:
    print(doubled_number)
    doubled_number *= 2