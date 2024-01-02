import pygame
def move(screen, x,y):
    playimg = pygame.image.load("../img/objects/player.png")
    screen.blit(playimg, (x, y))