import pygame
from Sprites import Sprite


class Wall(Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface([20, 20])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x


