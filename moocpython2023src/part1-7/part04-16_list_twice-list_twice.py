# Write your solution here
num_list = []
num = -100
while num != 0:
    num = int(input("New item: "))

    if num != 0:
        num_list.append(num)
        print(f"The list now: {num_list}")
        print(f"The list in order: {sorted(num_list)}")
    
print("Bye!")

