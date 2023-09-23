# WRITE YOUR SOLUTION HERE:
# create analog clock

import pygame
import math
import time

def convert_to_coordinate(center_x, center_y, radius, theta):
    full_circle = 360
    clock_angle = 2 * math.pi * (theta / full_circle)
    y = math.cos( clock_angle)*(radius)-center_y
    x = center_x+math.sin(clock_angle)*(radius)
    return x, -y

def main():
     # initialize pygame 
    pygame.init() 

    # window dimension
    window_width = 640
    window_height = 480

    # create window for game 
    window = pygame.display.set_mode((window_width, window_height))
    
    center_x = window_width // 2
    center_y = window_height // 2
    
    full_circle = 360
    interval = 60
   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        times = time.localtime()
        current_hour = times.tm_hour
        current_minute = times.tm_min
        current_seconds = times.tm_sec
        
        window.fill((0, 0, 0))
        pygame.display.set_caption(f"{current_hour}:{current_minute}:{current_seconds}")
        radius = 200
        thickness = 4
        pygame.draw.circle(window, (255, 0, 0), (center_x, center_y), radius, thickness)
        
        pygame.draw.circle(window, (255, 0, 0), (center_x, center_y), 10)

        # seconds
        # subract the radius of a second's handle by 10 from previous circle radius
        radius -= 10
        # calculate a theta or angle from origin to next number for second's handle
        theta = current_seconds*(full_circle/interval)
        # calculate or convert the next header of a second handle 
        header_x, header_y = convert_to_coordinate(center_x, center_y, radius, theta)
        # thickness handle will be 2 
        thickness = 2
        pygame.draw.line(window, (255, 0, 255), (center_x, center_y), (header_x, header_y), thickness)

        # minute
        radius -= 5
        theta = (current_minute+(current_seconds/interval))*(full_circle/interval)
        header_x, header_y = convert_to_coordinate(center_x, center_y, radius, theta)
        thickness = 3
        pygame.draw.line(window, (0, 255, 255), (center_x, center_y), (header_x, header_y), thickness)

        # hour
        radius -= 20
        theta = (current_hour + (current_minute/interval) + (current_seconds/(interval**2))) * (full_circle/12)
        header_x, header_y = convert_to_coordinate(center_x, center_y, radius, theta)
        thickness = 5
        pygame.draw.line(window, (255, 255, 255), (center_x, center_y), (header_x, header_y), thickness)

        pygame.display.flip()
        time.sleep(1)
main()