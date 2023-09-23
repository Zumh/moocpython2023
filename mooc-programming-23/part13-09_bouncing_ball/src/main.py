# WRITE YOUR SOLUTION HERE:

# Please create an animation where a ball bounces from the edges of the window

import pygame

def main():
    pygame.init()
    window_width = 640
    window_height = 480
    window = pygame.display.set_mode((window_width, window_height))
    ball = pygame.image.load("ball.png")
    diameter = ball.get_width()
    clock = pygame.time.Clock()
    frame_per_second = 60
    speed = 3
    x = 0
    x_velocity = speed
    y = 0 
    y_velocity = speed


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() 


        window.fill((0,0,0))
        
        window.blit(ball,(x,y))

        # check condition 
        if x >= window_width - diameter:
            x_velocity = -speed
        elif x == 0:
            x_velocity = speed
        if y >= window_height - diameter:
            y_velocity = -speed
        elif y == 0:
            y_velocity = speed
        x += x_velocity
        y += y_velocity
        pygame.display.flip()
        
        clock.tick(frame_per_second)
        
main()