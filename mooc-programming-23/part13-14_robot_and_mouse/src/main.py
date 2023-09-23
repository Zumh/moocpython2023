# WRITE YOUR SOLUTION HERE:
"""
Please write a program where the robot follows the mouse cursor so that the centre of the robot is always directly at the mouse cursor.
"""
import pygame
def get_new_coordinate(coordinate, dimension):
    target_value = coordinate
    target_value = max(target_value, 0)
    target_value = min(target_value, dimension)

    return target_value
def main():
    pygame.init()
    window = pygame.display.set_mode((640, 480))

    robot = pygame.image.load("robot.png")

    robot_width = robot.get_width()
    robot_height = robot.get_height()
    window_width = window.get_width()
    window_height = window.get_height()

    end_window_width = window_width - robot_width
    end_window_height = window_height - robot_height
    robot_x = 0
    robot_y = 0
    target_x = 0
    target_y = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                target_x = event.pos[0]-robot.get_width()/2
                target_y = event.pos[1]-robot.get_height()/2

            if event.type == pygame.QUIT:
                exit(0)
        robot_x = get_new_coordinate(target_x, end_window_width)
        robot_y = get_new_coordinate(target_y, end_window_height)
            

        window.fill((0, 0, 0))
        window.blit(robot, (robot_x, robot_y))
        pygame.display.flip()

        clock.tick(60)
main()