import pygame
import time
from Sprites import Sprite


# Construction of character
class Player(Sprite):
    def __init__(self, posargs, width, height, colour):
        self.x = posargs[0]
        self.y = posargs[1]
        Sprite.__init__(self, self.x, self.y, width, height, colour)
        self.vel = 3
        self.jumping = False

    # defines the movement controls for the players
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += self.vel

        if keys[pygame.K_a]:
            self.rect.x -= self.vel

        if keys[pygame.K_s]:
            self.rect.y += self.vel

        if keys[pygame.K_w] and self.jumping == False:
            self.jumping = True
            self.jump()
            if self.keyCheck(keys):
                self.jumping = False

    def setPos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def getPos(self):
        return [self.rect.x, self.rect.y]

    '''########    #      #       #
       #           #        #   #
       ###         #          #
       #           #        #   #
       #           #      #       #'''

    def jump(self):
        jumpheight = self.vel * 4
        while jumpheight >= -(self.vel * 4):
            print(jumpheight)
            print(self.rect.y)
            self.rect.y -= jumpheight
            jumpheight -= self.vel

    def keyCheck(self, keys):
        if keys[pygame.K_w]:
            return False
        return True
