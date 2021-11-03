import pygame
from Sprites import Sprite


# Construction of character
class Player(Sprite):
    def __init__(self, posargs, width, height, colour):
        self.x = posargs[0]
        self.y = posargs[1]
        Sprite.__init__(self, self.x, self.y, width, height, colour)
        self.vel = 5
        self.upVel = 30
        self.jumping = False
        self.gravity = 5
        self.falling = False
        self.dead = False

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += self.vel

        if keys[pygame.K_a]:
            self.rect.x -= self.vel

    def jump(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.jumping is False and self.falling is False:
                self.rect.y -= self.upVel

    def notCollide(self):
        self.rect.y += self.gravity
        self.falling = True

    def setPos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def getPos(self):
        return [self.rect.x, self.rect.y]

    def checkBounds(self):
        if self.rect.y >= 520:
            self.dead = True

        if self.rect.x < 0:
            self.dead = True

        elif self.rect.x >= 480:
            self.rect.x = 480
