import pygame
import random


def forest(screen, y, f_tab):
    grove = pygame.image.load("../img/objects/forest.png")
    for i in range(3):
        print(f_tab[i])
        if f_tab[i] != 0:
            screen.blit(grove, (400*i, 1800-y))
    return f_tab


def randomise_forest():
    side = random.randint(0,3)
    if side == 0:
        long = random.randint(1, 5)
        return [0, long, 0], long
    elif side == 1:
        long = random.randint(1, 5)
        return [long, 0, 0], long
    elif side == 2:
        long = random.randint(1, 5)
        return [0, 0, random.randint(1, 5)], long
    else:
        left_long = random.randint(1,5)
        right_long = random.randint(1,5)
        if left_long >= right_long:
            return [left_long, 0, right_long], left_long
        else:
            return [left_long, 0, right_long], right_long

