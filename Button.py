import pygame

displayWidth = 500
displayHeight = 500

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

pygame.font.init()

def textObjects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


# used to display text
def messageDisplay(text):
    text = pygame.font.Font('freesansbold.ttf', 50)
    textSurf, textRect = textObjects(text, text)
    textRect.center = ((displayWidth / 2), (displayHeight / 2))
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()

class Button:
    def __init__(self, function, surface, posx, posy, width, height, colour, text):
        self.rect = pygame.Rect(posx, posy, width, height)
        self.colour = colour
        self.surface = surface
        self.function = function
        self.text = text
        pygame.draw.rect(self.surface, self.colour, self.rect)

    def mouseCheck(self):
        mouse = pygame.mouse.get_pos()

        if self.rect.x + self.rect.width > mouse[0] > self.rect.x and\
                self.rect.y + self.rect.height > mouse[1] > self.rect.y:
            pygame.draw.rect(self.surface, bright_green, self.rect)
            self.buttonText()

            if pygame.mouse.get_pressed()[0]:
                self.function()

        else:
            pygame.draw.rect(self.surface, self.colour, self.rect)
            self.buttonText()

    def buttonText(self):
        text = pygame.font.Font('freesansbold.ttf', 30)
        textSurf, textRect = textObjects(self.text, text)
        textRect.center = ((self.rect.x + 50), (self.rect.y + 25))
        self.surface.blit(textSurf, textRect)
