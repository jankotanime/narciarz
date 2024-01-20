import pygame
import random

grove = pygame.image.load("../img/objects/new_forest.png")
pond = pygame.image.load("../img/objects/ice.png")


def forest(screen, y, f_tab):
    if f_tab['type'] == 1:
        x = 0
    elif f_tab['type'] == 2:
        x = 400
    elif f_tab['type'] == 3:
        x = 800
    else:
        screen.blit(grove, (0, f_tab['start'] - y))
        screen.blit(grove, (800, f_tab['start'] - y))
        return -180, 180, f_tab['start'] - 150, f_tab['start'] + 640
    screen.blit(grove, (x, f_tab['start'] - y))
    return x-620, x-180, f_tab['start'] - 150, f_tab['start'] + 640


def death_function(x, y, mig):
    if mig['x1'] < x < mig['x2'] and mig['y1'] < y < mig['y2']:
        return 1


def ice_function(x, y, mig):
    if mig['x1'] < x < mig['x2'] and mig['y1'] < y < mig['y2']:
        return 1


def death_border_function(x, y, mig):
    if (mig['x1'] > x or x > mig['x2']) and mig['y1'] < y < mig['y2']:
        return 1


def randomise_forest():
    side = random.randint(1, 4)
    return side


def randomise_ice(filled):
    if filled == 4:
        return 2
    side = filled['type']
    while filled['type'] != side:
        side = random.randint(1, 3)
    return side


def ice(screen, y, f_tab):
    if f_tab['type'] == 1:
        x = 0
    elif f_tab['type'] == 2:
        x = 400
    else:
        x = 800
    screen.blit(pond, (x, f_tab['start'] - y))
    return x-620, x-180, f_tab['start'] - 150, f_tab['start'] + 640
