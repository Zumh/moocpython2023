# Write your solution here
key_editor = "visual studio code"
editor = ""
while editor != key_editor:
    editor = input("Editor: ").lower()

    if editor == "visual studio code":
        print("an excellent choice!")
    elif editor == "notepad" or editor == "word":
        print("awful")
    else:
        print("not good")