__author__ = "Trang Ha"
import pygame
from pygame import mixer
import random
import math

# Initialize and customize the screen
pygame.init()
gameMode = True
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("spaceBackground.jpg")
pygame.display.set_caption("xSpace")
mixer.music.load("background.wav")
mixer.music.play(-1)


# Set up space ship
ssImg = pygame.image.load("ufo.png")
ssX, ssY, spaceCoor = 370, 480, 0
def spaceShip(x, y):
    screen.blit(ssImg, (x, y))

# Set up target X
xImg =[]
x, y, xCoor =[], [], []

for i in range(6):
    xImg.append(pygame.image.load("monster.png"))
    x.append(random.randint(0, 736))
    y.append(random.randint(50, 150))
    xCoor.append(1)
def targetX(x, y, i):
    screen.blit(xImg[i], (x, y))

# Set up fire
fireImg = pygame.image.load("fire.png")
fireX, fireY, fireCoor, fireMode = 0, 480, 8, "off"
def fire(x, y):
    global fireMode
    fireMode = "on"
    screen.blit((fireImg), (x + 16, y + 10))

# Collision
def isCollision(x, y, fireX, fireY):
    distance = math.sqrt(math.pow(x - fireX, 2) + math.pow(y - fireY, 2))
    if distance < 30:
        return True
    else:
        return False

scoreVal = 0
scoreFont = pygame.font.Font("freesansbold.ttf", 32)
textX, textY = 10, 10
def showScore(x, y):
    score = scoreFont.render("Score: " + str(scoreVal), True, (255, 255, 255))
    screen.blit(score, (x, y))

gaveOverFont = pygame.font.Font("freesansbold.ttf", 64)
def gameOver():
    gameOver = gaveOverFont.render("Game over", True, (255, 255, 255))
    screen.blit(gameOver, (200, 250))

while gameMode:
    # Screen background
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameMode = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceCoor = -3
            elif event.key == pygame.K_RIGHT:
                spaceCoor = 3
            elif event.key == pygame.K_SPACE:
                # The next bullet will be fired until the last bullet reached y-axis
                if fireMode is "off":
                    fireSound = mixer.Sound("gunShot.wav")
                    fireSound.play()
                    fireX = ssX
                    fire(fireX, fireY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spaceCoor = 0


    ssX += spaceCoor
    # Set boundary for space ship
    if ssX <= 0:
        ssX = 0
    elif ssX > (800-64):
        ssX = (800-64)

    # X movement
    for i in range(6):
        # Game over
        if y[i] > 400:
            for j in range(6):
                y[j] = 2000
            gameOver()
            break
        x[i] += xCoor[i]
        if x[i] <= 0:
            xCoor[i] = 1
            y[i] += 40
        elif x[i] > (800-64):
            xCoor[i] = -1
            y[i] += 40

        # Collision
        collision = isCollision(x[i], y[i], fireX, fireY)
        if collision:
            fireY = 480
            fireMode = "off"
            x[i], y[i] = random.randint(0, 736), random.randint(50, 150)
            scoreVal += 1
        targetX(x[i], y[i],i)

    # Fire movement
    if fireY <= 0:
        fireY = 480
        fireMode = "off"
    elif fireMode is "on":
        fire(fireX, fireY)
        fireY -= fireCoor


    spaceShip(ssX, ssY)
    showScore(textX, textY)
    pygame.display.update()