import pygame, sys
import os
import time
import random

#load ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))

#player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))

#lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

pygame.init()
pygame.font.init()
width, height = 750, 750
win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Space Adventure!")

#background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (width, height))

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
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()