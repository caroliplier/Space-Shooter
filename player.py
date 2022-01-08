import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,xcon,ycon,speed):
        super().__init__()
        self.speed = speed
        self.x_max = xcon
        self.y_max = ycon
        self.ready = True
        self.laser_time = 0
        self.laser_cd = 600
        self.dash_time = 500
        self.dash_cd = 1000
        self.image = pygame.image.load('assets/pixel_ship_yellow_up2.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)

        self.lasers = pygame.sprite.Group()

    #keybindings
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    #dashing
        if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
            self.rect.x += self.speed/2
        if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
            self.rect.x -= self.speed/2
        if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
            self.rect.y -= self.speed/2
        if keys[pygame.K_s] and keys[pygame.K_LSHIFT]:
            self.rect.y += self.speed/2
    
    #limit of lasers per sec
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cd:
                self.ready = True

    #spaceship(player) constraint
    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.x_max:
            self.rect.right = self.x_max
        if self.rect.top <= self.y_max - self.y_max/3:
            self.rect.top = self.y_max - self.y_max/3
        if self.rect.bottom >= self.y_max:
            self.rect.bottom = self.y_max
    
    #lasers shooting
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center,10,self.rect.bottom))

    #updates
    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()