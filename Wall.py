import pygame
from Sprites import Sprite


class Wall(Sprite):
    def __init__(self, x, y):
        self.xPos = x
        self.yPos = y
        self.width = 20