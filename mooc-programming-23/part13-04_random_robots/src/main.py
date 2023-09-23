# WRITE YOUR SOLUTION HERE:
# Please write a program which draws a thousand robots in random places.

import pygame
from random import randint

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

for row_count in range(1000):
    # randomize x location and y location
    x = randint(0,window_x - robot_width)
    y = randint(0, window_y - robot_height)


    window.blit(robot,(x, y))





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