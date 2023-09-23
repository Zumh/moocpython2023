# WRITE YOUR SOLUTION HERE:

# Please write a program where the player can move a robot in four directions with the arrow keys on the keyboard.
import pygame 

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

    # keys 
    key_events = {pygame.K_LEFT:-speed,pygame.K_RIGHT:speed,pygame.K_UP:-speed,pygame.K_DOWN:speed}
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
        
        if key_press in [pygame.K_LEFT,pygame.K_RIGHT]:
            x += key_events[key_press]
        elif key_press in [pygame.K_UP,pygame.K_DOWN]:
            y += key_events[key_press]

        # fill the background color
        window.fill(background_color)
      
        # draw a robot on the window
        window.blit(robot, (x, y))

        # update the content
        pygame.display.flip()

    
        
        clock.tick(frame_per_seconds)

main()