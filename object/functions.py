import pygame
import object.obstacles as obstacles


def chart(screen, x, y):
    map = pygame.image.load("../img/objects/map.png")
    screen.blit(map, (0, 0 - y))
    map_top = pygame.image.load("../img/objects/map_top.png")
    screen.blit(map_top, (0, 1800 - y))
    obstacles.forest(screen, 0 - y)
    player = pygame.image.load("../img/objects/player.png")
    screen.blit(player, (560 + x, 80))
    obstacles.forest(screen, y)


def move(screen, x, y, n, forest_long, kier):
    f_long = forest_long
    if kier == 1:
        x -= n
    elif kier == 2:
        x += n
    if y%150 == 0:
        if forest_long == 0:
            f_long = obstacles.randomise_forest()[1]
            print(f_long)
        else:
            f_long = forest_long - 1
    chart(screen, x, y + n)
    if y + n >= 1800:
        return [x, 0, n+1, kier]
    return [x, y + n, n, f_long, kier]


def lost(game):
    return 0
