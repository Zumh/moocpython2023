# WRITE YOUR SOLUTION HERE:
# Please create an animation where two robots move back and forth to the left and right. The lower robot should move at double the speed of the upper one

import pygame 
def calculate_velocity(robot_distance: int,  end_of_window: int, velocity: int):
    
    if robot_distance == end_of_window:
        velocity = -1
    elif robot_distance == 0:
        velocity = 1
    return velocity

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

    

    # robot dimension
    robot_width = robot.get_width()
    robot_height = robot.get_height()

    robot_1 = {'x':0, 'y':robot_height}
    robot_2 = {'x':0, 'y':robot_height*2}

    bot1_velocity = 1
    bot2_velocity = 1

    # set up clock
    clock = pygame.time.Clock()

    # frame per seconds
    frame_per_seconds = 60

    # running window time frame
    while True:

        # search for window event that make a window quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # set up window back ground color with black
        window.fill((0,0,0))
        
        # draw a robot 1
        window.blit(robot, (robot_1['x'], robot_1['y']))

        # draw a robot 2
        window.blit(robot, (robot_2['x'], robot_2['y']))
 
        # update pygame with content 
        pygame.display.flip()
        
        # increment the velocity of robot one
        robot_1['x'] += bot1_velocity

        # double the speed of robot 2
        robot_2['x'] += bot2_velocity * 2

        bot1_velocity = calculate_velocity(robot_1['x'], window_width - robot_width, bot1_velocity)
        bot2_velocity = calculate_velocity(robot_2['x'], window_width - robot_width, bot2_velocity)
   
        # make the clock tick for 60 seconds
        clock.tick(frame_per_seconds)

main()

   

   
    
   
