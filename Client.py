import pygame
from Network import Network
from Player import Player

# Create game display
displayWidth = 500
displayHeight = 500
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Client")
spriteList = pygame.sprite.Group()

# Main Program
def main():
    pygame.init()
    run = True
    n = Network()
    # gets base position for player
    myPlayerPosition = n.getP()
    otherPlayerPosition = (0,0)
    myPlayer = Player(myPlayerPosition,20,20,(255,0,0))
    otherPlayer = Player((otherPlayerPosition),20,20,(0,0,255))
    spriteList.add(myPlayer)
    spriteList.add(otherPlayer)
    Clock = pygame.time.Clock()

    while run:
        otherPlayerPosition = n.send(myPlayerPosition)
        spriteList.update()
        spriteList.sprites()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

        myPlayer.move()
        gameDisplay.fill((255,255,255))
        spriteList.draw(gameDisplay)

        pygame.display.update()

        Clock.tick(60)
main()