# Write your solution here

numb_list = [1,2,3,4,5]
index = value = 0
while index >= 0:
    
    index = int(input("Index: "))
    if index >= 0 and 0 <= index < len(numb_list):
        value = int(input("New value: "))
        numb_list[index] = value
        print(numb_list)
