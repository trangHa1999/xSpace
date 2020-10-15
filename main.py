__author__ = "Trang Ha"
import pygame, random

# Initialize and customize the screen
pygame.init()
gameMode = True
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("spaceBackground.jpg")
pygame.display.set_caption("xSpace")

# Set up space ship
ssImg = pygame.image.load("ufo.png")
ssX, ssY, spaceCoor = 370, 480, 0
def spaceShip(x, y):
    screen.blit(ssImg, (x, y))

# Set up target X
xImg = pygame.image.load("monster.png")
x, y, xCoor = random.randint(0, 800), random.randint(50, 150), 2
def targetX(x, y):
    screen.blit(xImg, (x, y))

# Set up fire
fireImg = pygame.image.load("fire.png")
fireX, fireY, fireCoor = ssX, 480, 0

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
    x += xCoor
    if x <= 0:
        xCoor = 2
        y += 40
    elif x > (800-64):
        xCoor = -2
        y += 40
    spaceShip(ssX, ssY)
    targetX(x, y)
    pygame.display.update()




