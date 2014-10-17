import sys

import pygame
from pygame.locals import *
import gopher

pygame.init()
clock = pygame.time.Clock()

window_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('PyCon Frogger')

colors = {
    'black': pygame.Color(0, 0, 0)
}

while True:
    window_surface.fill(colors['black'])

    # window_surface.blit(gopher_obj.image, gopher_obj.pos)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        else:
            # tutaj obslugujemy obiekty

    pygame.display.update()
    clock.tick(30)