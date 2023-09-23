# WRITE YOUR SOLUTION HERE:

import pygame 
from random import randint


def new_coordinate(asteroid_coordinate: dict, new_width: int, new_height: int):
    asteroid_coordinate['x'] = randint(0, new_width)
    asteroid_coordinate['y'] = -randint(0, new_height)

def main():
    pygame.init()
    # draw a window 
    window_width = 640
    window_height = 480

    window = pygame.display.set_mode((window_width, window_height))
    # draw a background with RGB
    window_back_ground = (0,0,0)
    
    # load robot image 
    robot = pygame.image.load("robot.png")
    # get the dimension of a robot 
    robot_width = robot.get_width()
    robot_height = robot.get_height()

    # ends 
    end_window_width = window_width - robot_width 
    end_window_height = window_height - robot_height 

    # center of the window 
    center_x = end_window_width / 2 

    # robot's location 
    robot_x, robot_y = center_x, end_window_height
    robot_velocity = 5

    key_press = 0
    event_keys = {pygame.K_LEFT: -robot_velocity, pygame.K_RIGHT: robot_velocity}

    # clock for for game 
    frame_per_seconds = 60
    clock = pygame.time.Clock()

    # asteroits 
    asteroid_velocity = 1
    total_asteroids = 10
    asteroids_coordinates = []

     # load asteroits 
    asteroid = pygame.image.load("rock.png")
    # get the dimension of a asteroid 
    asteroid_width = asteroid.get_width()
    asteroid_height = asteroid.get_height()

    # random location for asteroids 
    for count_asteroid in range(total_asteroids):
        new_asteroid = {'x':0, 'y':0}
        new_coordinate(new_asteroid, window_width - asteroid_width, window_height - asteroid_height)
        asteroids_coordinates.append(new_asteroid)

    # intialize score and write them on the window 
    score = 0
    score_font = pygame.font.SysFont("Arial", 24)
    # caption for asteroid
    pygame.display.set_caption("Asteroids")

    # listen to the event of pygame 
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() 

            # make sure key press is valid value
            if event.type == pygame.KEYDOWN:
                key_press = event.key
               
            if event.type == pygame.KEYUP:
                 key_press = 0

        window.fill(window_back_ground)
        
        # prepare the font size to update on the window
        score_format = f"Score: {score}"
        score_length = len(score_format)
      
        score_width = window_width - (score_length**(2.2))
        text = score_font.render(score_format, True, (255, 0, 0))
        window.blit(text, (score_width, 20))

        # draw asteroids with new location on the window
        for asteroids_coordinate in asteroids_coordinates:
            window.blit(asteroid,(asteroids_coordinate['x'],asteroids_coordinate['y']))

        # draw a robot on the screen 
        window.blit(robot,(robot_x, robot_y))

        # UPDATE GAME CONTENT 
        pygame.display.flip()

        # robot key press detections
        if key_press in event_keys.keys():
            robot_x += event_keys[key_press]
            if robot_x < 0: 
                robot_x = 0
            elif robot_x > end_window_width:
                robot_x = end_window_width

        
        # Update the position of the asteroids by adding its speed to its y-coordinate
        for asteroid_coordinate in asteroids_coordinates:
            # keep traveling until asteroid reach the ground
            asteroid_coordinate['y'] += asteroid_velocity
            # if they reach the ground, reinitialize rock position from the start 
            if asteroid_coordinate['y'] >= window_height - asteroid_height:
                # if the asteroids are out of the window then restart with new starting point
                new_coordinate(asteroid_coordinate, window_width - asteroid_width, window_height - asteroid_height)
            
       
        
            else:
          
                # robot's from left, right sides and asteroid's left, right side are within the boundary.
                # robot_y is the same as asteroid's bottom height

                robot_left = robot_x 
                robot_right = robot_x + robot_width
                robot_head = robot_y 
                asteroid_left = asteroid_coordinate['x']
                asteroid_right = asteroid_coordinate['x'] + asteroid_width
                asteroid_bottom = asteroid_coordinate['y'] + asteroid_height
                
             

                # if asteroid reach the dimension of the robot 
                if asteroid_bottom >= robot_head:
                    # asteroid left hit the right of robot
                    # asteroid hit robot from the left side
                    if (robot_right >= asteroid_right and robot_left <= asteroid_left) or (robot_left > asteroid_left and robot_left <= asteroid_right) or (robot_right < asteroid_right and robot_right >= asteroid_left):

                        # count the score and re intialize the asteroid's position
                        score += 1

                        # reinitialize asteroid position 
                        new_coordinate(asteroid_coordinate, window_width - asteroid_width, window_height - asteroid_height)
            
             
        
            

        clock.tick(frame_per_seconds)
      
main()

