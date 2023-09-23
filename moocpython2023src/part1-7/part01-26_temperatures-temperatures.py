"""
Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. 
If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

Two examples of expected behaviour:

Please type in a temperature (F): 101
101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

Please type in a temperature (F): 21
21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
Brr! It's cold in here!
"""

temperature_fahrenheit = int(input("Please type in a temperature (F): "))
temperature_celsius = (temperature_fahrenheit - 32) * (5/9)
temperature_result = f"{temperature_fahrenheit} degrees Fahrenheit equals {temperature_celsius} degrees Celsius"
if temperature_celsius < 0:
    temperature_result += "\nBrr! It's cold in here!"
print(temperature_result)