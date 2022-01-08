import pygame, sys
import os
from player import Player

pygame.init()
pygame.font.init()
width, height = 750, 750
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Space Adventure!")

#background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (width, height))

class Game:
    def __init__(self):
        player_sprite = Player((width/2,height))
        self.player = pygame.sprite.GroupSingle(player_sprite)
    def run(self):
        self.player.draw(win)

def main():
    run = True
    FPS = 60
    lv = 1
    lives = 5
    main_font = pygame.font.SysFont("impact", 50)

    clock = pygame.time.Clock()

    def redraw_window():
        win.blit(BG, (0,0))
        #texts
        lives_text = main_font.render(f"Lives : {lives}", 1, (255,255,255))
        lv_text = main_font.render(f"Level : {lv}", 1, (255,255,255))
        
        win.blit(lives_text, (10, 10))
        win.blit(lv_text,(width - lv_text.get_width() - 10,10))

        pygame.display.update()

    while run:
        win.fill((30,30,30))

        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()