# WRITE YOUR SOLUTION HERE:
"""
Please write a program where the robot appears at a random location within the window. 
When the player clicks on the robot with the mouse, the robot moves to a new location.
"""

import pygame
from random import randint

def main():
    pygame.init()
    window = pygame.display.set_mode((640, 480))

    robot = pygame.image.load("robot.png")

    robot_width = robot.get_width()
    robot_height = robot.get_height()
    window_width = window.get_width()
    window_height = window.get_height()

    end_window_width = window_width - robot_width
    end_window_height = window_height - robot_height
    robot_x_0 = 0
    robot_x_1 = robot_width
    robot_y_0 = 0
    robot_y_1 = robot_height
    

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                
                # update  the start of a robot position in random location if the mouse button position is within a robot dimension
                if robot_x_0 <= mouse_x <= robot_x_1 and robot_y_0 <= mouse_y <= robot_y_1:
                    
                    # update robot starting point
                    robot_x_0 = randint(0,end_window_width)
                    robot_y_0 = randint(0,end_window_height)

                    # update robot new end point
                    robot_x_1 = robot_x_0 + robot_width
                    robot_y_1 = robot_y_0 + robot_height
                    

            if event.type == pygame.QUIT:
                exit(0)

        
        window.fill((0, 0, 0))
        window.blit(robot, (robot_x_0, robot_y_0))
        pygame.display.flip()

        clock.tick(60)
main()