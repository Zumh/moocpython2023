"""
Please write a program which asks for the user's name. 
If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.
"""

name = input("Please type in your name: ")
user = ""
whos_nephews = "You're not a nephew of any character I know of."
if name == "Huey" or name == "Dewey" or name == "Louie":
    user = "Donald Duck"
elif name == "Morty" or name == "Ferdie":
    user = "Mickey Mouse"
if len(user) > 0:
    whos_nephews = f"I think you might be one of {user}'s nephews."
print(whos_nephews)