import pygame

def menu(screen):
    menuimg = pygame.image.load("../img/other/menu.png")
    screen.blit(menuimg, (0, 0))

def indicator(screen, n):
    cords=[176, 273, 487, 217, 243, 517, 258, 283, 478, 299, 301, 457]
    left = pygame.image.load("../img/other/left-arrow.png")
    right = pygame.image.load("../img/other/right-arrow.png")
    if n==-1: n=3
    if n==4: n=0
    for i in range(4):
        if i==n:
            screen.blit(left, (cords[n*3+1], cords[n*3]))
            screen.blit(right, (cords[n*3+2], cords[n*3]))
    return n


