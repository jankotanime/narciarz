import pygame
import object.obstacles as obstacles


def chart(screen, x, y):
    map = pygame.image.load("../img/objects/map.png")
    screen.blit(map, (0, 0 - y))
    map_top = pygame.image.load("../img/objects/map_top.png")
    screen.blit(map_top, (0, 1800 - y))
    player = pygame.image.load("../img/objects/player.png")
    screen.blit(player, (570 + x, 80))


def move(screen, x, y, n, forest_long, f_var, kier):
    chart(screen, x, y + n)
    if kier == 1:
        x -= n
    elif kier == 2:
        x += n
    if y%150 == 0:
        if forest_long == 0:
            f_tab = obstacles.randomise_forest()
            f_var = f_tab[0]
            forest_long = f_tab[1]
            print(f_var)
            print(f_tab)
        else:
            forest_long = forest_long - 1
    f_var = obstacles.forest(screen, y, f_var)
    if y + n >= 1800:
        return [x, 0, n, forest_long, f_var, kier]
    return [x, y + n, n, forest_long, f_var, kier]


def lost(game):
    return 0
