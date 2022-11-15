import imp
import pygame, sys
from settings import *
from tiles import Tile
from level import Level

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('temp1')
clock = pygame.time.Clock()
level = Level(map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("black")
    level.run()
    pygame.display.update()
    clock.tick(60)

