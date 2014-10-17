import pygame
from pygame.locals import *


class Object(object):
    pos = [0, 0]
    surface = None

    def __init__(self, surface):
        self.surface = surface

    def accept_event(event):
        pass
