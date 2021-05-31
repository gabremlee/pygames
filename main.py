import pygame
import random
import math
from pygame import mixer



pygame.init()

wn = pygame.display.set_mode((800, 600))

bg = pygame.image.load("bg.jpg")
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


player = pygame.image.load("ship.png")
px = 370
py = 500

alien = []
ax = []
ay = []
a = []
b = []
# alien = pygame.image.load("monster.png")
# a = random.randint(100, 700)
# ay = random.randint(50,300)

aliens = 6

for i in range(aliens):
    alien.append(pygame.image.load("monster.png"))
    ax.append(random.randint(100, 700))
    ay.append(random.randint(50, 300))
    a.append(4)
    b.append(20)

bullet = pygame.image.load("bullet.png")
bx = 0
by = py
bstate = "ready"

def ship(x, y):
    wn.blit(player, (x, y))

def aliena(x, y, i):
    wn.blit(alien[i], (x, y))

def p(x, y):
    global bstate
    bstate = "fired"
    wn.blit(bullet, (x+24, y))


#background sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#handling collisons
def collison(x, y, xa, xb):
    distance = math.sqrt((math.pow(xa-x,2))+(math.pow(xb-y,2)))
    if distance < 27:
        return True
    else:
        return False


score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
fx = 10
fy = 20

def show_score(x, y):
    scoret = font.render("score: "+ str(score), True, (255, 255, 255))
    wn.blit(scoret, (x, y))

def game_over():
    scoret = font.render("Game Over", True, (255, 255, 255))
    wn.blit(scoret, (400, 300))
run = True
# a = 2
# b = 20

while run:
    wn.fill((0, 0, 0))
    wn.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                px -= 40

            if event.key == pygame.K_RIGHT:
                px += 32

            if px >= 734:
                px = 734

            if px <= 0:
                px =0

            if event.key == pygame.K_UP:
                shoot = mixer.Sound("laser.wav")
                shoot.play()
                bx = px
                p(bx, by)


    for i in range(aliens):
        ax[i] += a[i]
        if ax[i] >= 734:
            a[i] = -3
            ay[i] += b[i]
        elif ax[i] <= 0:
            a[i] = 3
            ay[i] += b[i]

        collision = collison(ax[i], ay[i], bx, by)
        if collision:
            kill = mixer.Sound("explosion.wav")
            kill.play()
            by = py
            bstate = "ready"
            score += 1
            ax[i] = random.randint(100, 700)
            ay[i] = random.randint(50, 300)

        aliena(ax[i], ay[i] + b[i], i)
        if ay[i] >= 400:
            for j in range(aliens):
                ay[j] = 2000
            game_over()
            break;

    if by <= 0:
        by = py
        bstate = "ready"
    if bstate == "fired":
        p(bx, by)
        by -= 20



    ship(px, py)
    show_score(fx, fy)
    pygame.display.update()