import pygame
from ClientConnection import ClientConnection
from Player import Player
from Wall import Wall

# Create game display
displayWidth = 500
displayHeight = 500
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Client")
platformSpriteList = pygame.sprite.Group()
playerSpriteList = pygame.sprite.Group()

# Define colours

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

pygame.font.init()


def textObjects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def messageDisplay(text):
    text = pygame.font.Font('freesansbold.ttf', 50)
    textSurf, textRect = textObjects(text, text)
    textRect.center = ((displayWidth / 2), (displayHeight / 2))
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()


def lobby():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        buttonPos = (200, 350, 100, 50)
        gameDisplay.fill((255, 255, 255))
        pygame.draw.rect(gameDisplay, (0, 255, 0), buttonPos)
        text = pygame.font.Font('freesansbold.ttf', 50)
        textSurf, textRect = textObjects("Network Jump", text)
        textRect.center = ((displayWidth / 2), (displayHeight / 2))
        gameDisplay.blit(textSurf, textRect)

        mouse = pygame.mouse.get_pos()

        if 200 + 100 > mouse[0] > 200 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(gameDisplay, bright_green, buttonPos)

            if pygame.mouse.get_pressed()[0]:
                main()
        else:
            pygame.draw.rect(gameDisplay, green, buttonPos)

        pygame.display.update()


# Main Program
def main():
    # Upon connection receives player position from server.
    connection = ClientConnection()
    myPlayerPosition = connection.connect()
    otherPlayerPosition = (0, 0)

    pygame.init()

    # Initialises player sprites
    myPlayer = Player(myPlayerPosition, 20, 20, (255, 0, 0))
    otherPlayer = Player(otherPlayerPosition, 20, 20, (0, 0, 255))

    startFloor = Wall(0, 480, 500, 20, (0, 0, 0))
    startWall = Wall(0, 0, 20, 480, (0, 0, 0))
    startRoof = Wall(0, 0, 480, 20, (0, 0, 0))

    platformSpriteList.add(startFloor)
    platformSpriteList.add(startWall)
    platformSpriteList.add(startRoof)

    playerSpriteList.add(otherPlayer)
    playerSpriteList.add(myPlayer)

    clock = pygame.time.Clock()

    run = True
    while run:
        myPlayerPosition = myPlayer.getPos()
        otherPlayerPosition = connection.send(myPlayerPosition)
        otherPlayer.setPos(otherPlayerPosition)

        myPlayer.scrollPlayer()
        for i in platformSpriteList.sprites():
            i.scroll()

        platformSpriteList.update()
        playerSpriteList.update()


        while pygame.sprite.spritecollideany(myPlayer, platformSpriteList) is None:
            myPlayer.checkCollide()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        myPlayer.move()
        gameDisplay.fill((255, 255, 255))
        platformSpriteList.draw(gameDisplay)
        playerSpriteList.draw(gameDisplay)

        pygame.display.update()

        clock.tick(60)
    pygame.quit()
    exit()


lobby()
