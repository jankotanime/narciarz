import pygame
import random


def forest(screen, y):
    grove = pygame.image.load("../img/objects/forest.png")
    screen.blit(grove, (200, y + 600))



def randomise_forest():
    forests = []
    amount = random.randint(1,3)
    fun_long = 0
    for i in range(amount):
        forests.append([])
        type = random.randint(1, 4)
        long = random.randint(0, 4)
        forests[i].append(type)
        forests[i].append(long)
        if forests[i][1] > fun_long:
            fun_long = forests[i][1]
    return forest, fun_long

