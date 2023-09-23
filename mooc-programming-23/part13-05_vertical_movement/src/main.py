# WRITE YOUR SOLUTION HERE:
# make robot move vertical

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




# get the dimensions of the robot in pixels unit
robot_width = robot.get_width()
robot_height = robot.get_height()



x = 0
y = 0
is_up = False
while True:
    # return list of event from events collected
    for event in pygame.event.get():

        # Quit event is raise when window exits by clicking
        if event.type == pygame.QUIT:

            # program exit with exit function
            # Ctrl + C can also be use here
            exit()

    # fill method fills window with colour passed as argument
    window.fill((0,0,0))

    window.blit(robot,(0, y))

    # flip update the window with contents
    pygame.display.flip()
    
    bottom_left = window_y-robot_height
    if bottom_left <= y:  
        is_up = True
    elif y <= 0:
        is_up = False
    # going up is true than we increment up direction
    # if going up is false then we go down direction
    if is_up: 
        y -= 1
    else:
        y += 1
    
    pygame.time.Clock().tick(60)
    