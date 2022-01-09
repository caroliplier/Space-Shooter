import pygame
import sys

from player import Player
from background import Background
from alien import Alien
from random import choice
from laser import Laser

pygame.display.set_caption('Space Adventure!')

class Game:
    def __init__(self):
        #background setup
        bg_sprite = Background((0,0))
        self.background = pygame.sprite.GroupSingle(bg_sprite)
        
        #player setup
        player_sprite = Player((screen_width/2,screen_height),screen_width,screen_height,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        #alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
        self.alien_direction = 1
        self.alien_lasers = pygame.sprite.Group()

    def alien_setup(self,rows,cols,x_distance = 60,y_distance = 50,x_offset = 150, y_offset = 100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                
                if row_index == 0: alien_sprite = Alien('yellow',x,y)
                elif row_index <= 2: alien_sprite = Alien('green',x,y)
                else: alien_sprite = Alien('red',x,y)
                self.aliens.add(alien_sprite)
    
    def alien_move_down(self,distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_pos_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)
    
    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center,6,screen_height)
            self.alien_lasers.add(laser_sprite)

    def run(self):
        self.background.draw(screen)
        
        self.alien_pos_checker()
        self.aliens.update(self.alien_direction)
        self.player.update()
        
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.aliens.draw(screen)

if __name__ == '__main__':
    pygame.init()
    screen_width = 750
    screen_height = 750
    screen = pygame.display.set_mode((screen_width,screen_height))

    clock = pygame.time.Clock()
    FPS = 60
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill ((30,30,30))
        game.run()
        
        pygame.display.update()
        clock.tick(FPS)
