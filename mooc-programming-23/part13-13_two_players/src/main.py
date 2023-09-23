# WRITE YOUR SOLUTION HERE:
"""
Please write a program where two players each direct their own robot. 
One of the players should use the arrow keys while the other could use, for example, the w-s-a-d keys
"""

import pygame 
def get_new_coordinate(key_event, type_speed, key_press, window_dimension):
    key_event[type_speed] += key_event[key_press]
    key_event[type_speed] = max(key_event[type_speed],0)
    key_event[type_speed] = min(key_event[type_speed],window_dimension)
   
def main():
    pygame.init()

    # background color 
    background_color = (0,0,0)
    # init window dimension
    window_height = 480
    window_width = 640
    window_dimensions = (window_width, window_height)
    
    # create a window 
    window = pygame.display.set_mode(window_dimensions)

    # initialize the coordinate of a robot
    x = 0
    y = 0

    speed = 2

    # initialize the clock here 
    clock = pygame.time.Clock()
    
    # create a robot 
    robot = pygame.image.load("robot.png")
    # get the robot width and height 
    robot_width = robot.get_width()
    robot_height = robot.get_height()

    # calculate end of window 
    end_window_width = window_width - robot_width
    end_window_height = window_height - robot_height

    # keys 
    key_events = {
        ('bot1','x'):{'x_speed':0, pygame.K_LEFT:-speed,pygame.K_RIGHT:speed},
        ('bot1','y'):{'y_speed':0, pygame.K_UP:-speed,pygame.K_DOWN:speed},
        
        ('bot2','x'):{'x_speed':0, pygame.K_a:-speed,pygame.K_d:speed},
        ('bot2','y'):{'y_speed':0, pygame.K_w:-speed,pygame.K_s:speed}}
 
    key_press = 0

    # fps 
    frame_per_seconds = 60
    while True:

        for event in pygame.event.get():
            
            # check keyboard input 
            key_event_type = event.type
            if key_event_type == pygame.KEYDOWN:
                key_press = event.key
            if key_event_type == pygame.QUIT:

                # if the window is press quit then quit from the window 
                exit() 
        
        if key_press in key_events[('bot1', 'x')].keys():
            # within the window range
            get_new_coordinate(key_events[('bot1','x')], 'x_speed', key_press, end_window_width)
        elif key_press in key_events[('bot1', 'y')].keys():
            get_new_coordinate(key_events[('bot1','y')], 'y_speed', key_press, end_window_height)
        
        elif key_press in key_events[('bot2', 'x')].keys():
            # within the window range
            get_new_coordinate(key_events[('bot2','x')], 'x_speed', key_press, end_window_width)
        elif key_press in key_events[('bot2', 'y')].keys():
            get_new_coordinate(key_events[('bot2','y')], 'y_speed', key_press, end_window_height)


            
        # fill the background color
        window.fill(background_color)
        
        # draw a robot on the window
        window.blit(robot, (key_events[('bot1','x')]['x_speed'], key_events[('bot1','y')]['y_speed']))

        # draw a robot on the window
        window.blit(robot, (key_events[('bot2','x')]['x_speed'], key_events[('bot2','y')]['y_speed']))

        # update the content
        pygame.display.flip()

    
        
        clock.tick(frame_per_seconds)

main()
