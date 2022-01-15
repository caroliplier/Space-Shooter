import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self,colour,x,y):
        super().__init__()
        self.image = pygame.image.load('assets/' + colour + 'a.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))
    
        if colour == 'red' : self.value = 100
        elif colour == 'green' : self.value = 200
        else: self.value = 300

    def update(self,direction):
        self.rect.x += direction