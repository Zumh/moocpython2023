"""
Please write a program which asks the user for a password. 
The program should then ask the user to type in the password again. 
If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

Password: sekred
Repeat password: secret
They do not match!
Repeat password: cantremember
They do not match!
Repeat password: sekred
User account created!
"""

password = input("Password: ")
pass_match = "User account created!"
repeat_password = ""
while password != repeat_password:
    repeat_password = input("Repeat password: ")
    if password != repeat_password:
        pass_match = "They do not match!"
    else:
        pass_match = "User account created!"
    print(pass_match)