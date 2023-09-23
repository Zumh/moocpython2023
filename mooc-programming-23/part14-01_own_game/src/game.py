import pygame
from random import randint
 
class CollectingGame:
    '''
    Goal of the game is to collect 10 coins avoiding monsters, after you collect all 10 coins a door will appear on the robot starting coordinates
    '''
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.robot = pygame.image.load("robot.png")
        self.coin = pygame.image.load("coin.png")
        self.monster = pygame.image.load("monster.png")
        self.door = pygame.image.load("door.png")
        self.x = 320 - self.robot.get_width()/2
        self.y = 480 - self.robot.get_height()
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption('Collecting Game')
        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False
        self.open_door = False
        self.game_over = False
        self.grats = True
        self.new_game()
        self.main_loop()
 
            
    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            if self.open_door:
                if self.is_collided_with((self.x, self.y), (320 - self.door.get_width()/2, 480 - self.door.get_height())):
                    self.game_over = True
            if self.grats == False:
                break
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_UP:
                    self.to_up = True
                if event.key == pygame.K_DOWN:
                    self.to_down = True
                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
                if event.key == pygame.K_UP:
                    self.to_up = False
                if event.key == pygame.K_DOWN:
                    self.to_down = False
            if event.type == pygame.QUIT:
                exit()
        if self.to_right:
            self.x += 2 if self.x < 640-self.robot.get_width() else 0
        if self.to_left:
            self.x -= 2 if self.x > 0 else 0
        if self.to_up:
            self.y -= 2 if self.y > 0 else 0
        if self.to_down:
            self.y += 2 if self.y < 480-self.robot.get_height() else 0
        if self.is_collided_with((self.x, self.y), self.coincoord):
            self.score += 1
            self.coincoord = self.generate_new_coin_location()
        
        for monster in self.monsters:
            if self.is_collided_with((self.x, self.y), monster):
                self.new_game()
                
        self.move_monsters()
        self.text = self.game_font.render(f"Score: {self.score}", True, (255, 0, 0))
        if self.score >= 10:
            self.open_door = True
 
    def new_game(self):
        self.score = 0
        self.coincoord = self.generate_new_coin_location()
        self.x = 320 - self.robot.get_width()/2
        self.y = 480 - self.robot.get_height()
        self.monsters = [[0, 0], [640-self.monster.get_width(), 100], [0, 200]]
        self.velocity = 1
        self.center_monster_velocity = 1
 
    def move_monsters(self):  
            self.monsters[0][0] += self.velocity
            self.monsters[2][0] += self.velocity
            self.monsters[1][0] += self.center_monster_velocity
            if self.velocity > 0 and self.monsters[0][0]+self.monster.get_width() >= 640:
                self.velocity = -self.velocity
            if self.velocity< 0 and self.monsters[0][0] <= 0:
                self.velocity = -self.velocity
            if self.velocity > 0 and self.monsters[0][0]+self.monster.get_width() >= 640:
                self.velocity = -self.velocity
            if self.velocity < 0 and self.monsters[0][0] <= 0:
                self.velocity= -self.velocity
            if self.center_monster_velocity > 0 and self.monsters[1][0]+self.monster.get_width() >= 640:
                self.center_monster_velocity = -self.center_monster_velocity
            if self.center_monster_velocity< 0 and self.monsters[1][0] <= 0:
                self.center_monster_velocity = -self.center_monster_velocity
            if self.center_monster_velocity > 0 and self.monsters[1][0]+self.monster.get_width() >= 640:
                self.center_monster_velocity = -self.center_monster_velocity
            if self.center_monster_velocity < 0 and self.monsters[1][0] <= 0:
                self.center_monster_velocity= -self.center_monster_velocity
              
    def generate_new_coin_location(self):
        if self.score < 10:
            return randint(0, 640-self.coin.get_width()), randint(0, 480-self.coin.get_height())
        else:
            return (-100, -100)
    
    def is_collided_with(self, robot_coordinates, coin_coordinates):
        rect1 = self.robot.get_rect(topleft=robot_coordinates)
        rect2 = self.coin.get_rect(topleft=coin_coordinates)
        return rect1.colliderect(rect2)
            
    def draw_window(self):
        if self.game_over:
            self.window.fill((0, 0, 255))
            
            if self.grats == True:
                for i in range(10):
                    self.window.blit(self.game_font.render(f"Congratulations", True, (randint(0, 255), randint(0, 255), randint(0, 255))), (randint(0, 640-150), randint(0, 480-150)))
                    pygame.display.flip()
                    pygame.time.wait(500)
                self.grats = False
 
        else:
            self.window.fill((0, 0, 255))
            self.window.blit(self.robot, (self.x, self.y))
            self.window.blit(self.coin, self.coincoord)
            for i in self.monsters:
                self.window.blit(self.monster, i)
            self.window.blit(self.text, (500, 20))
            if self.open_door:
                self.window.blit(self.door, (320 - self.door.get_width()/2, 480 - self.door.get_height()))
        pygame.display.flip()
        self.clock.tick(60)
 
if __name__ == "__main__":
    CollectingGame()