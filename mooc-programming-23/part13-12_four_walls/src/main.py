# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:

# Please improve the program in the previous exercise so that the robot cannot pass outside the window in any of the four directions.
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

    # calculate end of window 
    end_window_width = window_width - robot_width
    end_window_height = window_height - robot_height

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
            # within the window range
            
            x += key_events[key_press]
            x = max(x,0)
            x = min(x,end_window_width)

        elif key_press in [pygame.K_UP,pygame.K_DOWN]:
            y += key_events[key_press]
            y = max(y,0)
            y = min(y,end_window_height)

            
        # fill the background color
        window.fill(background_color)
      
        # draw a robot on the window
        window.blit(robot, (x, y))

        # update the content
        pygame.display.flip()

    
        
        clock.tick(frame_per_seconds)

main()


"""
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
x = width/2-robot.get_width()/2
y = height/2-robot.get_height()/2
 
to_right = False
to_left = False
to_up = False
to_down = False
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
 
        if event.type == pygame.QUIT:
            exit()
 
    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_up:
        y -= 2
    if to_down:
        y += 2
 
    x = max(x,0)
    x = min(x,width-robot.get_width())
    y = max(y,0)
    y = min(y,height-robot.get_height())
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()
 
    clock.tick(60)
"""