import pygame
import object.obstacles as obstacles

main_map = pygame.image.load("../img/objects/map.png")
player = pygame.image.load("../img/objects/player.png")


def chart(screen, x, y):
    screen.blit(main_map, (0, 0 - y))
    screen.blit(main_map, (0, 1800 - y))
    screen.blit(player, (570 + x, 80))


def move(screen, x, y, n, score, objects, kier):
    death_zone = {'x1': -465, 'x2': 465, 'y1': 0, 'y2': 1800}
    death_objects = []
    chart(screen, x, y + n)
    if kier == 1:
        x -= n
    elif kier == 2:
        x += n
    if y == 0:
        objects[0]['type'] = obstacles.randomise_forest()
        objects[0]['start'] = 900
        objects[1]['start'] = 0
    if y == 900:
        objects[1]['type'] = obstacles.randomise_forest()
        objects[1]['start'] = 1800
    death = obstacles.forest(screen, y, objects[0])
    death_objects.append({'x1': death[0], 'x2': death[1], 'y1': death[2], 'y2': death[3]})
    death = obstacles.forest(screen, y, objects[1])
    death_objects.append({'x1': death[0], 'x2': death[1], 'y1': death[2], 'y2': death[3]})

    death = obstacles.death_border_function(x, y, death_zone)

    for i in range(len(death_objects)):
        if death == 1:
            break
        if objects[i]['type'] != 4:
            death = obstacles.death_function(x, y, death_objects[i])
        else:
            death = obstacles.death_border_function(x, y, death_objects[i])

    if death == 1:
        n = lost(n)

    if y + n >= 1800:
        return [x, 0, n, score, objects]
    return [x, y + n, n, score, objects]


def lost(game):
    return 0
