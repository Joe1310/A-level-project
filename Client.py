import pygame
from ClientConnection import ClientConnection
from Player import Player

# Create game display
displayWidth = 500
displayHeight = 500
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Client")
spriteList = pygame.sprite.Group()


# Main Program
def main():

    startPos = (displayWidth / 2, 200)
    connection = ClientConnection()
    myPlayerPosition = connection.connect()
    otherPlayerPosition = (0,0)
    # gets base position for player
    pygame.init()
    myPlayer = Player(myPlayerPosition, 20, 20, (255, 0, 0))
    otherPlayer = Player((otherPlayerPosition), 20, 20, (0, 0, 255))
    spriteList.add(otherPlayer)
    spriteList.add(myPlayer)

    Clock = pygame.time.Clock()

    run = True
    while run:
        myPlayerPosition = myPlayer.getPos()
        otherPlayerPosition = connection.send(myPlayerPosition)
        otherPlayer.setPos(otherPlayerPosition)
        spriteList.update()
        spriteList.sprites()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        myPlayer.move()
        gameDisplay.fill((255, 255, 255))
        spriteList.draw(gameDisplay)

        pygame.display.update()

        Clock.tick(60)
    pygame.quit()
    exit()


main()
