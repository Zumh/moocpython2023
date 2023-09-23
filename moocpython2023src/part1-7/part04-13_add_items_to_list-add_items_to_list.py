# Write your solution here

amount_item = int(input("How many items: "))
count_item = 0 
item_list = []
while count_item < amount_item:
    item_list.append(int(input(f"Item {count_item + 1}: "))
)
    count_item += 1
print(item_list)