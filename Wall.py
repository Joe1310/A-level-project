import pygame
from Sprites import Sprite


class Wall(Sprite):
    def __init__(self, x, y, width, height, colour):
        Sprite.__init__(self, x, y, width, height, colour)



