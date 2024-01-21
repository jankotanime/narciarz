import pygame
import random

grove = pygame.image.load("../img/objects/new_forest.png")
pond = pygame.image.load("../img/objects/ice.png")
skier = pygame.image.load("../img/objects/skier.png")


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
    return x - 620, x - 180, f_tab['start'] - 150, f_tab['start'] + 640


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
    if filled['type'] == 4:
        return 2
    if filled['type'] == 1:
        return random.randint(2, 3)
    elif filled['type'] == 3:
        return random.randint(1, 2)
    else:
        side = random.randint(1, 2)
        if side == 1:
            return 1
        return 3


def ice(screen, y, f_tab):
    if f_tab['type'] == 1:
        x = 0
    elif f_tab['type'] == 2:
        x = 400
    else:
        x = 800
    screen.blit(pond, (x, f_tab['start'] - y))
    return x - 620, x - 180, f_tab['start'] - 150, f_tab['start'] + 180


def randomise_skier(filled):
    if filled['type'] == 4:
        return 2, random.randint(1, 4)
    side = filled['type']
    while side == filled['type']:
        side = random.randint(1, 3)
    placement = random.randint(1, 4)
    return side, placement


def ski(screen, y, f_tab):
    if f_tab['type'][0] == 1:
        x = 0 + f_tab['type'][1] * 60
    elif f_tab['type'][0] == 2:
        x = 400 + f_tab['type'][1] * 60
    else:
        x = 800 + f_tab['type'][1] * 60
    screen.blit(skier, (x, f_tab['start'] - y * 0.8))
    return x - 610, x - 520, f_tab['start']-120, f_tab['start']


def conflict(x, y, mig):
    if mig['x1'] < x < mig['x2'] and mig['y1'] < y * 0.8 < mig['y2']:
        return 1
