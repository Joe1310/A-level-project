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
        playerSpriteList.update()

        while pygame.sprite.spritecollideany(myPlayer, platformSpriteList) is None:
            myPlayer.checkCollide()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        myPlayer.move()
        gameDisplay.fill((255, 255, 255))
        platformSpriteList.draw(gameDisplay)
        playerSpriteList.draw(gameDispl ay)

        pygame.display.update()

        clock.tick(60)
    pygame.quit()
    exit()


main()
