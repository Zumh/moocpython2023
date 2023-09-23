"""
Let's create a program along the lines of the example above. 
This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". 
Then the program should print out "okay then" and finish. Please have a look at the example below.
"""

greet = ""
greet_back = "hi"
while greet != "no":
    print(greet_back)
    greet = input("Shall we continue? ")

    if greet == "no":
        greet_back = "okay then"
print(greet_back)
