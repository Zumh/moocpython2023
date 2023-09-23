# Write your solution here
num_list = []
commands = ""

value = 1
while commands != "x":
    print(f"The list is now {num_list}")
    commands = input("a(d)d, (r)emove or e(x)it: ")
    command = commands.lower()
    if command == "d":
        num_list.append(value)
        value += 1
    elif command == "r":
        value = num_list.pop()
print("Bye!")

