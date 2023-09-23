# # WRITE YOUR SOLUTION HERE:

import pygame


# initialize pygame object
pygame.init()

robot = pygame.image.load("robot.png")

# get window dimension 
window_x = 640
window_y = 480

# set up a window size 
window = pygame.display.set_mode((window_x, window_y))

# get clock
clock = pygame.time.Clock()

# robot dimension 
robot_width = robot.get_width()
robot_height = robot.get_height()

# get top right corner
end_x = window_x - robot_width 

# get bottom left corner 
end_y = window_y - robot_height

# initialize distance 
x = 0
y = 0
velocity = 1
# check for event 
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # draw the background color RGB 
    window.fill((0,0,0))

     # draw a new robot location 
    window.blit(robot,(x,y))

    # get the new location for robot
    # direction that we need to check 

     
    # top right corner to bottom right
    if x == end_x and y < end_y:
        # going down
        y += velocity
    
    # bottom right corner to bottom left
    elif y == end_y and x > 0:
        # going left 
        x -= velocity

    # top left corner to top right corner
    elif y == 0:
        # going right
        x += velocity    
    # bottom left corner to top left corner
    elif x == 0:
        # going up
        y -= velocity
  
    
    
        
   

    # update content 
    pygame.display.flip()
    
    # clock tick for 60 seconds
    clock.tick(60)