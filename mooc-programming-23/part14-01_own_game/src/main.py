"""
Project: A rain of coins 
Author: Zumhliansang Lungler
Date: Febuary, 25, 2023
Description: 
    This game is a copy idea from "A rain of coins". 
    The game have some help menu to start the game. 
    p for Play, x for Quit and left or right  arrows for moving side to side.
    The game can be play till level 3. As the game level goes up, it get faster and faster.
    A person with most coins or score is winner while avoiding monsters.
    Since we are not allow include other files. I suggest you play some kind of background music.
    https://www.youtube.com/watch?v=ApreCAQiZ4w
"""
# Complete your game here
import pygame

from random import randint
class Monster:
    """
        This is a monster class that handle monster sprite specifically.
        It handle monter position in a window. Also relocate in a random location.
    """
    def __init__(self, monster, window_width, window_height) -> None:
        self.__monster = monster
        self.__end_window_width = window_width - self.__monster.get_width()
        self.__end_window_height = window_height - self.__monster.get_height()
        self.re_locate()
    def pygame_monster(self):
        return self.__monster
    def re_locate(self):
        self.__x = randint(0, self.__end_window_width )
        self.__y = -randint(0, self.__end_window_height)
    
    def move_monster(self, speed):
        """
        moving a coin in the vertical position
        if out of the window that move it to new location
        """
        self.__y += speed
        if self.__y >= self.__end_window_height:
           self.re_locate()

    def left(self):
        return self.__x
    
    def right(self):
        return self.__x + self.__monster.get_width()
    
    def bottom(self):
        return self.__y + self.__monster.get_height()

    def location(self):
        return (self.__x, self.__y)
    
class Coin:
    """
        This is a coin class that handle coin sprite specifically.
        It handle coin position in a window. Also relocate in a random location.
    """
    def __init__(self, coin, window_width, window_height) -> None:
        self.__coin = coin
        self.__end_window_width = window_width - self.__coin.get_width()
        self.__end_window_height = window_height - self.__coin.get_height()
        self.re_locate()
    
    def coin_pygame(self):
        return self.__coin

    def re_locate(self):
        self.__x = randint(0, self.__end_window_width )
        self.__y = -randint(0, self.__end_window_height)
    
    def move_coin(self, speed):
        """
        moving a coin in the vertical position
        if out of the window that move it to new location
        """
        self.__y += speed
        if self.__y >= self.__end_window_height:
           self.re_locate()
    
    def left(self):
        return self.__x
    
    def right(self):
        return self.__x + self.__coin.get_width()
    
    def bottom(self):
        return self.__y + self.__coin.get_height()

    def location(self):
        return (self.__x, self.__y)
    

class Robot:
    """
    This robot class handle a robot movements, scores and life_line.
    Also relocate the robot in the middle of a window and lower bottom of the window.
    """
    def __init__(self, robot, window_width, window_height, life_line, scores) -> None:
        # get the loaded pygame robot from MonsterInvasion class
        self.robot = robot
        self.scores = scores
        # robot life line will equal to number of total robot from each level 
        self.life = life_line

        # robot movement left and right will be track here 
        self.end_of_width = (window_width  - self.robot.get_width())//2
        self.end_of_height = window_height - self.robot.get_height()

        # initialize location for x and y coordinate of a robot
        self.re_locate()

        # check life or death with boolean
        self.is_life= True 
    def robot_pygame(self):
        return self.robot
    def check_life(self):
        if self.life <= 0:
            self.is_life = False
            # making sure life is zero
            self.life = 0
        return self.is_life 

    def lost_life(self):
        self.life -= 1

    def move_robot(self, window_width, speed):
        """
        This robot move if robot location is within x window frame
        """
        end_of_window_width = window_width - self.robot.get_width()
        self.x += speed
        if self.x < 0: 
            self.x = 0
        elif self.x >= end_of_window_width:
            self.x = end_of_window_width

    def robot_location(self):
        return (self.x, self.y)
    
    def update_total_score(self, scores):
        self.scores += scores

    def robot_left(self):
        return self.x
    
    def robot_right(self):
        return self.x + self.robot.get_width()
    
    def robot_head(self):
        return self.y
    
    def re_locate(self):
        # robot movement left and right will be track here 
        self.x = self.end_of_width
        self.y = self.end_of_height
    

class MonsterInvasion:

    """
    This class will handle all the logics for playing the game.
    The class handle the appropriate algorithm to make other classes to interact each other.
    It also output a total score and each level score.
    """
    def __init__(self):
        pygame.init()
        self.monster_amount = 5
        self.monsters = []
        self.coins = []
        self.life_line = self.monster_amount
        self.robot_speed = 4
        self.speed = 1
        self.key_press = 0
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.scores = 0
        self.level = 1
        self.font = pygame.font.SysFont("Arial", 24)
        self.level_up = False 
        self.max_level = 3
        self.play = False

        self.red = 255
        self.green = 255
        self.blue = 255
        
        # load images and use those images to create object for each 
        
        self.window_height = 480
        self.window_width = 640 

        self.robot = Robot(pygame.image.load("robot.png"), self.window_width, self.window_height, self.life_line, self.scores)
        
        # get collection of monsters
        for count in range(self.monster_amount):
            self.monsters.append(Monster(pygame.image.load("monster.png"),self.window_width, self.window_height))
            self.coins.append(Coin(pygame.image.load("coin.png"),self.window_width, self.window_height))
              
        # intialize the window dimension       
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        pygame.display.set_caption("A rain of coins")

        self.main_loop()
   
    def main_loop(self):
        """
        This is a main loop the start event and draw all the sprite.
        Where everything start
        """
        while True:

            self.check_events()
            self.draw_window()

            self.clock.tick(self.fps)
    def draw_score(self):
        # prepare the font size to update on the window
        score_format = f"Score: {self.scores}"
        score_length = len(score_format)
      
        score_width = self.window_width - (score_length**(2.2))
        text = self.font.render(score_format, True, (255, 0, 0))
        self.window.blit(text, (score_width, 20))
    
    def draw_lifeline(self):
        # this class draw a life line for the robot
        # prepare the font size to update on the window
        format = f"Lives: {self.robot.life}"
        text = self.font.render(format, True, (255, 0, 0))
        self.window.blit(text, (1, 20))

    def draw_level(self):
        # draw the level number achieve
        
        # prepare the font size to update on the window
        format = f"Level: {self.level}"
        text = self.font.render(format, True, (255, 0, 0))
        self.window.blit(text, (1, 40))

    def check_events(self):
        """
        Make sure the right flag is up when event happen.
        """
        for event in pygame.event.get():
            # close the window if click x symbol
            if event.type == pygame.QUIT:
                exit()
            
            # close the window if press x
            if event.type == pygame.KEYDOWN:
                if pygame.K_x == event.key:
                    exit()
                if pygame.K_p == event.key:
                    self.play = True
                    # start a new game by re-initialize everything
                    self.new_game()
                
                self.key_press = event.key
            if event.type == pygame.KEYUP:
                self.key_press = 0
        # check robot key press 
        if pygame.K_LEFT == self.key_press:
            self.robot.move_robot(self.window_width, -self.robot_speed)
        elif pygame.K_RIGHT == self.key_press:
            
            self.robot.move_robot(self.window_width, self.robot_speed)

    def new_game(self):
        """
        Reinitialize everything 
        """
        self.monster_amount = 5
        self.robot.life = self.monster_amount
        self.life_line = self.monster_amount
        # empty score 
        self.scores = 0

        # reinitialize level 
        self.level = 1 

        self.speed = 1

        # reiintialize level_up 
        self.level_up = False 

        self.robot.re_locate()
        
        # relocate monsters location
        for monster in self.monsters:
            monster.re_locate()

        # relocate coin location 
        for coin in self.coins: 
            coin.re_locate() 

                
        
    def help_menu(self):
        """
        This function will show the help menu for the user
        """
        format = f"x = quit p = play Left+Right arrows = moves"
        text = self.font.render(format, True, (255, 0, 0))
        self.window.blit(text, (1, self.window_height//2))

    
    def draw_window(self):
        # white background
        
        back_ground = (self.red, self.green, self.blue)

        self.window.fill(back_ground)
        if self.level > self.max_level:
            # show total score 
            self.scores = self.robot.scores
        # draw score font
        self.draw_score()

        # draw lives line
        self.draw_lifeline()

        self.draw_level()

        if self.play == False:
            self.help_menu()
        
       
        if self.robot.life <= 0:
            result = f"Game over"
            result = self.font.render(result, True, (255, 0, 0))
            self.window.blit(result, (self.window_width//2,100))

            # stop everything 
            self.play = False

            # show play again -> re-initialize everything
            # or quit
            self.help_menu()
            
        elif self.level > self.max_level:
            
            # stop everything 
            self.play = False
            self.help_menu()

        elif self.level_up == True:
            # increment level
            self.level += 1
            # transfer score to total score
            self.robot.scores += self.scores
            self.scores = 0
            # double monster
            self.monster_amount *= 2
            self.life_line *= 2
            self.robot.life = self.life_line
            self.speed += 1
            # set level_up false 
            self.level_up = False
        elif self.play == True:
            # make it flashy background
            self.red = randint(0,255)
            self.green = randint(0,255)
            self.blue = randint(0,255) 
            # draw robot
            self.window.blit(self.robot.robot_pygame(), self.robot.robot_location())

            # draw monsters
            for monster in self.monsters:
                self.window.blit(monster.pygame_monster(), monster.location())
                self.update_life_line(monster)
                monster.move_monster(self.speed)

            # draw coin
            for coin in self.coins: 
                self.window.blit(coin.coin_pygame(), coin.location())
                self.update_score(coin)
                if self.scores ==  self.monster_amount:
                    # signal send to update level and reinitialize
                    self.level_up = True 
                    break
                coin.move_coin(self.speed)
            
            


        # update the content 
        pygame.display.flip()
    def count_score(self):
        # count the score 
        self.scores += 1

    def update_score(self, coin):
        """
        Up date the robot's score if a robot touch the coin
        """
        # if coin reach the dimension of the robot 
        if coin.bottom() >= self.robot.robot_head():
            # coin left hit the right of robot
            # coin hit robot from the left side
            if (self.robot.robot_right() >= coin.right() and self.robot.robot_left() <= coin.left()) or ( self.robot.robot_left() > coin.left() and  self.robot.robot_left() <= coin.right()) or (self.robot.robot_right() < coin.right() and self.robot.robot_right() >= coin.left()):

                # lost life line if robot touch coin
                self.count_score()

                # reinitialize coin position 
                coin.re_locate()
    def update_life_line(self, monster):
        """
        Up date the robot's life if a monster touch him
        """
        # if monster reach the dimension of the robot 
        if monster.bottom() >= self.robot.robot_head():
            # monster left hit the right of robot
            # monster hit robot from the left side
            if (self.robot.robot_right() >= monster.right() and self.robot.robot_left() <= monster.left()) or ( self.robot.robot_left() > monster.left() and  self.robot.robot_left() <= monster.right()) or (self.robot.robot_right() < monster.right() and self.robot.robot_right() >= monster.left()):

                # lost life line if robot touch monster
                self.robot.lost_life()

                # reinitialize monster position 
                monster.re_locate()
        
if __name__ == "__main__":
    play = MonsterInvasion()
