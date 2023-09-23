"""
In the Python math module there is the function sqrt, which calculates the square root of a number. 
You can use it like so:
from math import sqrt

print(sqrt(9))
This should print out

3.0

We will return to the concept of a module and the import statement later. For now, it is sufficient to understand that the line from math import sqrt allows us to use the sqrt function in our program.

Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

x = (-b ± sqrt(b²-4ac))/(2a).

You can assume the equation will always have two real roots, so the above formula will always work.

An example of expected behaviour:

Value of a: 1
Value of b: 2
Value of c: -8

The roots are 2.0 and -4.0
"""

# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

a_value = int(input("Value of a: "))
b_value = int(input("Value of b: "))
c_value = int(input("Value of c: "))

x_plus = ((-b_value)+sqrt((b_value**2)-(4*a_value*c_value)))/(2*a_value)
x_minus = ((-b_value)-sqrt((b_value**2)-(4*a_value*c_value)))/(2*a_value)

print(f"The roots are {x_plus} and {x_minus}")
# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5