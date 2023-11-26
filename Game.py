import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Game/space.png")
pygame.display.set_icon(icon)

# variables positions
player_positionsX = 370
player_positionsY = 480

# Player
playerImg = pygame.image.load("Game/player.png")
playerX = player_positionsX
playerY = player_positionsY
playerX_change = 0
playerY_change = 0

# ennemy
ennemyImg = pygame.image.load("Game/alien.png")
ennemyX = random.randint(0, 736)
ennemyY = random.randint(0, 200)
ennemyX_change = 0.2
ennemyY_change = 40

# ennemy2
ennemyImg = pygame.image.load("Game/alien.png")
ennemyX2 = random.randint(0, 736)
ennemyY2 = random.randint(0, 200)
ennemyX2_change = 0.2
ennemyY2_change = 40

# bullet
bulletImg = pygame.image.load("Game/bullet.png")
bulletX = player_positionsX
bulletY = player_positionsY
bulletX_change = 0
bulletY_change = 0.4
bullet_state = "ready"

score = 0


def Player(x, y):
    screen.blit(playerImg, (x, y))


def Ennemy(x, y):
    screen.blit(ennemyImg, (x, y))

def Ennemy2(x, y):
    screen.blit(ennemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + -20))

#collision 1
def isCollision(ennemyX, ennemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(ennemyX - bulletX, 2)) + \
        (math.pow(ennemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

#collision 2
def isCollision(ennemyX2, ennemyY2, bulletX, bulletY):
    distance = math.sqrt(math.pow(ennemyX2 - bulletX, 2)) + \
        (math.pow(ennemyY2 - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                playerX_change -= 0.2
            if event.key == pygame.K_d:
                playerX_change += 0.2
            if event.key == pygame.K_z:
                playerY_change -= 0.2
            if event.key == pygame.K_s:
                playerY_change += 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_z:
                playerY_change = 0
                playerX_change = 0

    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 200:
        playerY = 200
    elif playerY >= 536:
        playerY = 536

    #1
    ennemyX += ennemyX_change
    if ennemyX <= 0:
        ennemyX_change = 0.2
        ennemyY += ennemyY_change
    elif ennemyX >= 736:
        ennemyX_change = -0.2
        ennemyY += ennemyY_change

    #2
    ennemyX2 += ennemyX2_change
    if ennemyX2 <= 0:
        ennemyX2_change = 0.2
        ennemyY2 += ennemyY2_change
    elif ennemyX2 >= 736:
        ennemyX2_change = -0.2
        ennemyY2 += ennemyY2_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(ennemyX, ennemyY, bulletX, bulletY)

    # Collision2
    collision2 = isCollision(ennemyX2, ennemyY2, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        ennemyX = random.randint(0, 736)
        ennemyY = random.randint(0, 200)

    if collision2:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        ennemyX2 = random.randint(0, 736)
        ennemyY2 = random.randint(0, 200)


    Ennemy(ennemyX, ennemyY)
    Ennemy2(ennemyX2, ennemyY2)
    Player(playerX, playerY)
    pygame.display.update()
