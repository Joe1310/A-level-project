import pygame
from ClientConnection import ClientConnection
from Player import Player

# Create game display
displayWidth = 500
displayHeight = 500
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Client")
everythingElseSpriteList = pygame.sprite.Group()
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

    playerSpriteList.add(otherPlayer)
    playerSpriteList.add(myPlayer)

    clock = pygame.time.Clock()

    run = True
    while run:
        myPlayerPosition = myPlayer.getPos()
        otherPlayerPosition = connection.send(myPlayerPosition)
        otherPlayer.setPos(otherPlayerPosition)
        playerSpriteList.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        myPlayer.move()
        gameDisplay.fill((255, 255, 255))
        playerSpriteList.draw(gameDisplay)

        pygame.display.update()

        clock.tick(60)
    pygame.quit()
    exit()


main()
