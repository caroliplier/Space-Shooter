import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self,colour,x,y):
        super().__init__()
        self.image = pygame.image.load('assets/' + colour + '.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))