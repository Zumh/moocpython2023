
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

# The program only consists of displaying a window and it runs until the user closes the window.

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
"""
# blit is use for drawing image with coordinate
window.blit(robot, (0, 0))
window.blit(robot, (300, 0))
window.blit(robot, (100, 200))
"""

# put the robot image in the center of a window
# get the dimensions of the robot in pixels unit
width = robot.get_width()
height = robot.get_height()

# calculate x and y coordinate for robot image 
mid_window_x = window_x//2
mid_window_y = window_y//2
mid_robot_width = width/2
mid_robot_height = height/2
# the difference of window's mid dimension and robot image gave us a center location
window.blit(robot, (mid_window_x - mid_robot_width, mid_window_y - mid_robot_height))

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