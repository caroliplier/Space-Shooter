import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,screen_height):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.laser_ycon = screen_height

    #destroy lasers
    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.laser_ycon+50:
            self.kill()

    #updates
    def update(self):
        self.rect.y -= self.speed
        self.destroy()