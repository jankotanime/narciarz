import pygame
import object.obstacles as obstacles

main_map = pygame.image.load("../img/objects/map.png")
player = pygame.image.load("../img/objects/player.png")


def chart(screen, x, y):
    screen.blit(main_map, (0, 0 - y))
    screen.blit(main_map, (0, 1800 - y))
    screen.blit(player, (570 + x, 80))


def move(screen, x, y, n, forest_long, forest_var, forest_start, forest_change, kier):
    chart(screen, x, y + n)
    if kier == 1:
        x -= n
    elif kier == 2:
        x += n
    if y % 300 == 0:
        forest_long = forest_long - 1
    if forest_long == 0:
        if forest_change == 1:
            forest_tab = obstacles.randomise_forest()
            forest_var[0] = forest_tab[0][1]
            forest_var[1] = forest_tab[0][2]
            forest_long = forest_tab[1]
            forest_start = y + 600
            forest_change = 1
        else:
            forest_tab = obstacles.randomise_forest()
            forest_var[2] = forest_tab[0][1]
            forest_var[3] = forest_tab[0][2]
            forest_start = y + 1200
            forest_change = 0
    obstacles.forest(screen, y, forest_var, forest_start)
    if y + n >= 1800:
        return [x, 0, n, forest_long, forest_var, forest_start, kier]
    return [x, y + n, n, forest_long, forest_var, forest_start, kier]


def lost(game):
    return 0
