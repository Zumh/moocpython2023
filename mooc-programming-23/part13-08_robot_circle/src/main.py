# WRITE YOUR SOLUTION HERE:

# Please create an animation where ten robots go round in a circle.

import pygame
import math 


def main():
    # initialize pygame 
    pygame.init() 

    # window dimension
    window_width = 640
    window_height = 480

    # create window for game 
    window = pygame.display.set_mode((window_width, window_height))



    # get the robot image from current directory
    robot = pygame.image.load("robot.png")

    
    # frame per seconds
    frame_per_seconds = 60


    speed = 0.01
    robot_amount = 10

    # robot dimension
    robot_width = robot.get_width()
    robot_height = robot.get_height()

    robots_coordinate = []

    # set up clock
    clock = pygame.time.Clock()

    radius = 100

    # intialize robots 
    for count_robot in range(robot_amount):
        # Set the initial position and angle of each robot
        """
        This line finds the angle of the robot on the circle, in radians. 
        Radians are a way of measuring angles using the length of the curve and the length of the line from the center of the circle. 
        One radian is equal to the angle that makes a curve of the same length as the line from the center. 
        There are 2 * math.pi radians in a full circle, where math.pi is the value of pi, which is about 3.14. 
        The code multiplies 2 * math.pi by the number of the robot (count_robot) and divides by the total number of robots (robot_amount) to get the angle of each robot.
        """
        robot_angle = count_robot * ((2 * math.pi) / robot_amount)

        """
        This line finds the x-coordinate of the robot on the circle. 
        The x-coordinate is the distance from the center of the circle to the right or left. 
        The code uses the math.cos word, which returns the cosine of the angle given in radians. 
        The cosine is a number that tells you how far the robot is from the center of the circle on the right or left. 
        The code multiplies the cosine of the robot angle by the length of the line from the center of the circle to get the x-coordinate from the center of the circle, which is 320 pixels from the left edge of the screen. 
        The code then takes away half of the robot width to put the robot on the circle.
        """
        x = 320+math.cos(robot_angle)*radius-robot_width/2

        """
        This line finds the y-coordinate of the robot on the circle. 
        The y-coordinate is the distance from the center of the circle to the top or bottom. 
        The code uses the math.sin word, which returns the sine of the angle given in radians. 
        The sine is a number that tells you how far the robot is from the center of the circle on the top or bottom. 
        The code multiplies the sine of the robot angle by the length of the line from the center of the circle to get the y-coordinate from the center of the circle, which is 240 pixels from the top edge of the screen. 
        The code then takes away half of the robot height to put the robot on the circle.
        """
        y  = 240+math.sin(robot_angle)*radius-robot_height/2
        robots_coordinate.append({'x':x, 'y':y})

    # running window time frame
    while True:

        # search for window event that make a window quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # set up window back ground color with black
        window.fill((0,0,0))
        
        # draw updated robot location
        for robot_coordinate in robots_coordinate:
            window.blit(robot, (robot_coordinate['x'],robot_coordinate['y']))

        # update pygame with content 
        pygame.display.flip()
        
        # update a new location for each robot with a new angle

        for count_robot, robot_coordinate in enumerate(robots_coordinate):
            # calculate a new angle for current robot from 0 - 2pi. Then we add the speed  
            robot_angle = count_robot * ((2 * math.pi) / robot_amount) + speed 

            # we find the center of x and y window then subract the mid width of a robot
            robot_coordinate['x'] = 320 + math.cos(robot_angle)*radius - (robot_width/2)

            # calculation apply to the height of a robot as well
            robot_coordinate['y']  = 240 + math.sin(robot_angle)*radius - (robot_height/2)

            # From the center of a window to center of a robot we manage to find a new location for each robot in motion

        

        # update speed
        speed += 0.01

        # make the clock tick for 60 seconds
        clock.tick(frame_per_seconds)

main()

