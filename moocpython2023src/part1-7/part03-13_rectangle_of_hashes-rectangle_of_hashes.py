"""
Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Sample output
Width: 10
Height: 3
##########
##########
##########
"""

width = int(input("Width: "))
height = int(input("Height: "))
character = "#"
count_height = 0
while count_height < height:
    print(character * width)
    count_height += 1