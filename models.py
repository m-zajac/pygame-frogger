import os

import pygame
from pygame.locals import *


class Frog(pygame.sprite.Sprite):
    pos = [0, 0]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image('transfrog.png', -1)

    def update(self):
        pass


# helpers

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    return image, image.get_rect()
