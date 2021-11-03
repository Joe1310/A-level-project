from Sprites import Sprite
import pygame


class Wall(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self, x, y, width, height, (0, 0, 0))
