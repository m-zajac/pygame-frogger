import sys

import pygame
from pygame.locals import *
import models

# init
pygame.init()
clock = pygame.time.Clock()

window_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('PyCon Frogger')

background = pygame.Surface(window_surface.get_size())
background = background.convert()
background.fill((250, 250, 250))

frog = models.Frog()
frog_sprite = pygame.sprite.RenderPlain((frog,))

if __name__ == '__main__':
    while True:
        clock.tick(60)

        # events
        for event in pygame.event.get():
            if event.type == QUIT:
                break

        frog_sprite.update()

        # draw
        window_surface.blit(background, (0, 0))
        frog_sprite.draw(window_surface)
        pygame.display.flip()
