# WRITE YOUR SOLUTION HERE:

# Please write a program which draws a hundred robots: ten rows with ten robots in each row.

# WRITE YOUR SOLUTION HERE:

# Please write a program which draws ten robots in a row. The end result should look like this:

import pygame

# initialize s the pygame modules 
pygame.init()

# initialize the windows dimensions
window_x = 640
window_y = 480

# The next one creates a window with the function
# set_mode function takes the window dimensions as a n argument.
window = pygame.display.set_mode((window_x,window_y))

# load image from direct source into variable robot
robot = pygame.image.load("robot.png")

# fill method fills window with colour passed as argument
window.fill((0,0,0))


# get the dimensions of the robot in pixels unit
robot_width = robot.get_width()
robot_height = robot.get_height()

for row_count in range(10):
    # row_offset offset the pic start drawing 10 pixel to the right 
    row_offset = row_count * 10
    for column in range(10):
        # column_offset push each image to the right by 40 pixel unit plus column 
        # this allow us to maintain the distance of each robot
        column_offset = 38 * column
        
        # we offset the height by 20px and we start drawing from height of robot pix position
        window.blit(robot,(robot_width + row_offset + column_offset, robot_height+20*row_count))

    





# flip update the window with contents
pygame.display.flip()

while True:
    # return list of event from events collected
    for event in pygame.event.get():

        # Quit event is raise when window exits by clicking
        if event.type == pygame.QUIT:

            # program exit with exit function
            # Ctrl + C can also be use here
            exit()