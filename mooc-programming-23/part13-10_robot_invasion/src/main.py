# WRITE YOUR SOLUTION HERE:
"""
Please create an animation where robots fall from the sky randomly. 
When a robot reaches the ground, it starts moving to the left or to the right, and finaly disappears off the screen. 
"""

import pygame
import random

def main():
    pygame.init()
    window_width = 640
    window_height = 480
    window_back_ground = (0,0,0)
    window = pygame.display.set_mode((window_width, window_height))
    robot = pygame.image.load("robot.png")
    robot_width = robot.get_width()
    robot_height = robot.get_height()
    robots_coordinate = []
    total_robot = 10

    clock = pygame.time.Clock()
    frame_per_second = 60
    speed = 3
    sides = [1,-1]

    end_window_width = window_width - robot_width
    end_window_height = window_height - robot_height

    for count_robot in range(total_robot):
        x = random.randint(0,end_window_width)
        y = -random.randint(0,end_window_height)
        robots_coordinate.append({'x':x, 'y':y, 'side':0})

    while True:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() 


        window.fill(window_back_ground)
            
        for robot_coordinate in robots_coordinate:
            # if a robot reach the ground y coordinate will stay the same and x coordinate will go to right or left
            window.blit(robot,(robot_coordinate['x'],robot_coordinate['y']))

        
    
        
        pygame.display.flip()

         # Update the position of the robot by adding its speed to its y-coordinate
        for robot_coordinate in robots_coordinate:
            if not (0 <= robot_coordinate['x'] <= end_window_width): 
                # if the robot is out of the window then restart with new starting point
                x = random.randint(0,end_window_width)
                y = -random.randint(0,end_window_height)
                robot_coordinate['x'] = x
                robot_coordinate['y'] = y  
            
            elif robot_coordinate['y'] < end_window_height:
                robot_coordinate['y'] += speed
            # if it reach the ground 
            elif robot_coordinate['y'] >= end_window_height:
                
                # if y coordinate reach the ground randomly move left or right
                if robot_coordinate['side'] not in sides:
                    # if robot coordinate doesn't have left or right then pick one
                    robot_coordinate['side'] = random.choice(sides)
                
                # go to the right
                if robot_coordinate['side'] == 1:
                    robot_coordinate['x'] += speed
                # go to the left
                elif robot_coordinate['side'] == -1:
                    robot_coordinate['x'] -= speed  
            
        clock.tick(frame_per_second)
        
main()


"""
import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
# number of robots (the same robots are reused)
number = 20
 
robots = []
for i in range(number):
    # causes the new random start position to be drawn immediately
    robots.append([-1000,height])
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    for i in range(number):
        if robots[i][1]+robot.get_height() < height:
            # the robot falls downwards
            robots[i][1] += 1
        else:
            if robots[i][0] < -robot.get_width() or robots[i][0] > width:
                # new random start point
                robots[i][0] = randint(0,width-robot.get_width())
                robots[i][1] = -randint(100,1000)
            elif robots[i][0]+robot.get_width()/2 < width/2:
                # the robot moves to the left
                robots[i][0] -= 1
            else:
                # the robot moves to the right
                robots[i][0] += 1
 
    screen.fill((0, 0, 0))
    for i in range(number):
        screen.blit(robot, (robots[i][0], robots[i][1]))
    pygame.display.flip()
 
    clock.tick(60)
"""