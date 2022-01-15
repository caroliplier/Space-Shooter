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
        
        #health and score setup
        self.lives = 3
        self.live_img = pygame.image.load('assets/pixel_ship_yellow_up.png').convert_alpha()
        self.live_xstart = screen_width - (self.live_img.get_size()[0] * 2 + 20)

        self.score = 0
        self.font = pygame.font.Font('assets/pixeled.ttf',20)

        #player setup
        player_sprite = Player((screen_width/2,screen_height),screen_width,screen_height,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        #alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
        self.alien_direction = 1
        self.alien_lasers = pygame.sprite.Group()

    def alien_setup(self,rows,cols,x_distance = 70,y_distance = 60,x_offset = 80, y_offset = 60):
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
            laser_sprite = Laser(random_alien.rect.center,-5,screen_height)
            self.alien_lasers.add(laser_sprite)

    def collision_checks(self):
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                aliens_hit = pygame.sprite.spritecollide(laser,self.aliens,True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    laser.kill()

        if self.alien_lasers:
            for laser in self.alien_lasers:
                if pygame.sprite.spritecollide(laser,self.player,False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        pygame.quit()
                        sys.exit()
        if self.aliens:
            for alien in self.aliens:
                if pygame.sprite.spritecollide(alien,self.player,False):
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_xstart + (live * (self.live_img.get_size()[0] + 10))
            screen.blit(self.live_img,(x,8))

    def display_score(self):
        score_surf = self.font.render(f'SCORE: {self.score}',False,'white')
        score_rect = score_surf.get_rect(topleft = (10,-10))
        screen.blit(score_surf,score_rect)
    
    def victory(self):
        if not self.aliens.sprites():
            victory_surf = self.font.render('You WON!',False,'gold')
            victory_rect = victory_surf.get_rect(center = (screen_width/2, screen_height/2))
            screen.blit(victory_surf,victory_rect)

    def run(self):
        self.background.draw(screen)
        
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        self.alien_pos_checker()
        self.aliens.update(self.alien_direction)
        self.alien_lasers.update()
        self.alien_lasers.draw(screen)
        self.aliens.draw(screen)
        
        self.collision_checks()

        self.display_lives()
        self.display_score()
        
        self.victory()

if __name__ == '__main__':
    pygame.init()
    screen_width = 750
    screen_height = 750
    screen = pygame.display.set_mode((screen_width,screen_height))

    clock = pygame.time.Clock()
    FPS = 60
    game = Game()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER,1200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER :
                game.alien_shoot()

        screen.fill ((30,30,30))
        game.run()
        
        pygame.display.update()
        clock.tick(FPS)
