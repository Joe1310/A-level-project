import pygame

# child class of pygame.sprite.Sprite
class Sprite(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

