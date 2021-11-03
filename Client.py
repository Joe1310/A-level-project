import pygame
from ClientConnection import ClientConnection
from Player import Player
from Wall import Wall
from Button import Button
import random


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


# used to display text
def messageDisplay(text):
    text = pygame.font.Font('freesansbold.ttf', 50)
    textSurf, textRect = textObjects(text, text)
    textRect.center = ((displayWidth / 2), (displayHeight / 2))
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()


# quits the game when run
def quit():
    pygame.quit()
    exit()


def startMenu():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # displays text on the screen and generates three buttons
        gameDisplay.fill((255, 255, 255))
        button1 = Button(waitForAll, gameDisplay, 100, 350, 100, 50, green, "start")
        button2 = Button(quit, gameDisplay, 300, 350, 100, 50, green, "quit")

        text = pygame.font.Font('freesansbold.ttf', 50)
        textSurf, textRect = textObjects("Network Jump", text)
        textRect.center = ((displayWidth / 2), (displayHeight / 2))
        gameDisplay.blit(textSurf, textRect)
        # checks to see if the button has been pressed
        button1.mouseCheck()
        button2.mouseCheck()

        pygame.display.update()

def waitForAll():
    waiting = True
    connection = ClientConnection()
    myPlayerPosition = connection.connect()

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # displays text on the screen
        gameDisplay.fill((255, 255, 255))
        text = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = textObjects("Waiting for other player", text)
        textRect.center = ((displayWidth / 2), (displayHeight / 2))
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        connected = connection.getPlayerCount()
        # waits for both players to be connected before starting the game
        if connected == 2:
            waiting = False
            main(connection, myPlayerPosition)


def deathScreen():
    dead = True

    while dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # displays text on the screen and generates a button
        gameDisplay.fill((255, 255, 255))
        button1 = Button(startMenu, gameDisplay, 200, 350, 100, 50, green, "menu")
        text = pygame.font.Font('freesansbold.ttf', 50)
        textSurf, textRect = textObjects("You Died", text)
        textRect.center = ((displayWidth / 2), (displayHeight / 2))
        gameDisplay.blit(textSurf, textRect)

        button1.mouseCheck()

        pygame.display.update()


def winScreen():
    winning = True

    while winning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # displays text on the screen and generates a button
        gameDisplay.fill((255, 255, 255))
        button1 = Button(startMenu, gameDisplay, 200, 350, 100, 50, green, "menu")
        text = pygame.font.Font('freesansbold.ttf', 50)
        textSurf, textRect = textObjects("You Won!", text)
        textRect.center = ((displayWidth / 2), (displayHeight / 2))
        gameDisplay.blit(textSurf, textRect)

        button1.mouseCheck()

        pygame.display.update()
        
# Main Program
def main(connection, myPlayerPosition):
    # Upon connection receives player position from server.
    otherPlayerPosition = (0, 0)

    pygame.init()

    # Initialises player sprites
    myPlayer = Player(myPlayerPosition, 20, 20, (255, 0, 0))
    otherPlayer = Player(otherPlayerPosition, 20, 20, (0, 0, 255))

    # Initialises Spawn Area
    for x in range(5):
        startFloor = Wall((100 * x), 480, 100, 20)
        platformSpriteList.add(startFloor)
    FirstPlat = Wall(520, 400, 80, 20)
    platformSpriteList.add(FirstPlat)

    # Adds player characters to sprite list
    playerSpriteList.add(otherPlayer)
    playerSpriteList.add(myPlayer)

    clock = pygame.time.Clock()

    run = True
    while run:
        # gets the position data of the other player in exchange for their own position. Also gives client its number
        myPlayerPosition = myPlayer.getPos()
        connectionData = connection.send(myPlayerPosition)
        otherPlayerPosition = connectionData[0]
        playerNumber = connectionData[1]
        otherPlayer.setPos(otherPlayerPosition)

        # generates a scrolling effect for the players and platforms to simulate the screen scrolling to the right
        myPlayer.scroll()
        for platform in platformSpriteList.sprites():
            platform.scroll()

            # if the platform is off the back of the screen it removes it from the sprite group,
            # which prevents it being redrawn
            if (platform.rect.x + platform.rect.width) < 0:
                platform.kill()

        if playerNumber == 0:
            if len(platformSpriteList) < 6:
                # generates a new platform based on the previous
                    lastPlatY = platformSpriteList.sprites()[4].rect.y
                    newPlatY = lastPlatY + (random.choice([-1, 1]) * 80)
                    if newPlatY == 560:
                        newPlatY = 400
                    if newPlatY == 0:
                        newPlatY = 160
                    connection.sendPlat(newPlatY)

                    # adds new platform to the sprite group to be drawn
                    newPlatform = Wall(520, newPlatY, 80, 20)
                    platformSpriteList.add(newPlatform)

        else:
            # gets the position of the new platform generated by the other client
            if len(platformSpriteList) < 6:
                newPlatY = connection.getPlat()
	      if len(platformSpriteList) < 6:
    	      newPlatY = connection.getPlat()
                if newPlatY == platformSpriteList.sprites()[4]:
                    newPlatY = connection.getPlat()
                # adds new platform to the sprite group to be drawn
                newPlatform = Wall(520, newPlatY, 80, 20)
                platformSpriteList.add(newPlatform)

        # updates the players and platforms
        platformSpriteList.update()
        playerSpriteList.update()
        
      # applies gravity to player character if the player character is not already colliding with a platform
        if pygame.sprite.spritecollideany(myPlayer, platformSpriteList) is None and myPlayer.dead is False:
            myPlayer.notCollide()
            myPlayer.checkBounds()
            if myPlayer.dead:
                run = False
                deathScreen()

        elif pygame.sprite.spritecollideany(myPlayer, platformSpriteList) is not None:
            myPlayer.falling = False

        # checks to see if the player is off the playable area
        myPlayer.checkBounds()

        # checks if the player is dead
        if myPlayer.dead:
            run = False
            deathScreen()

        # checks if the player has won
        if otherPlayer.rect.y > 500 or otherPlayer.rect.x < 0:
            run = False
            winScreen()


        # Handles exiting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        myPlayer.move()
        for i in range(5):

            playerSpriteList.update()
            playerSpriteList.draw(gameDisplay)
            myPlayer.jump()

        gameDisplay.fill((255, 255, 255))
        platformSpriteList.draw(gameDisplay)
        playerSpriteList.draw(gameDisplay)

        pygame.display.update()

        # sets max fps
        clock.tick(60)
    pygame.quit()
    exit()


startMenu()


