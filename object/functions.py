import random
import pygame
import object.obstacles as obstacles

main_map = pygame.image.load("../img/objects/map.png")
player = pygame.image.load("../img/objects/better_player.png")
player_left = pygame.image.load("../img/objects/better_player-left.png")
player_right = pygame.image.load("../img/objects/better_player-rigth.png")
grove = pygame.image.load("../img/objects/new_forest.png")
pond = pygame.image.load("../img/objects/ice.png")
skier_img = pygame.image.load("../img/objects/skier.png")
death_img = pygame.image.load("../img/objects/death_img.png")
forest_border = pygame.image.load("../img/objects/forest_border.png")


def chart(screen, y):
    screen.blit(main_map, (0, 0 - y))
    screen.blit(main_map, (0, 1800 - y))


def forest(screen, y):
    screen.blit(forest_border, (0, 0 - y))
    screen.blit(forest_border, (0, 1800 - y))


def player_chart(screen, x, kier):
    if kier == 0:
        screen.blit(player, (540 + x, 80))
    elif kier == 1:
        screen.blit(player_left, (570 + x, 80))
    else:
        screen.blit(player_right, (570 + x, 80))


def move(screen, x, y, n, score, objects, kier):
    death_zone = {'x1': -435, 'x2': 415, 'y1': 0, 'y2': 1800}
    death_objects = []
    ice_objects = []
    skiers = []
    chart(screen, y + n)
    if kier == 1:
        x -= n
    elif kier == 2:
        x += n
    if y == 0:
        objects[0]['type'] = obstacles.randomise_forest()
        objects[0]['start'] = 900
        objects[1]['start'] = 0
        objects[2]['type'] = obstacles.randomise_ice(objects[1])
        objects[2]['start'] = 600
        objects[4]['type'] = obstacles.randomise_skier((objects[0]))
        objects[4]['start'] = random.randint(900, 1350)
        objects[5]['start'] = 600
    if y == 900:
        objects[1]['type'] = obstacles.randomise_forest()
        objects[1]['start'] = 1800
        objects[3]['type'] = obstacles.randomise_ice(objects[0])
        objects[3]['start'] = 1500
        objects[5]['type'] = obstacles.randomise_skier((objects[1]))
        objects[5]['start'] = 2400

    ice = obstacles.ice(screen, y, objects[2], pond)
    ice_objects.append({'x1': ice[0], 'x2': ice[1], 'y1': ice[2], 'y2': ice[3]})
    ice = obstacles.ice(screen, y, objects[3], pond)
    ice_objects.append({'x1': ice[0], 'x2': ice[1], 'y1': ice[2], 'y2': ice[3]})

    player_chart(screen, x, kier)

    skier = obstacles.ski(screen, y, objects[4], skier_img)
    skiers.append({'x1': skier[0], 'x2': skier[1], 'y1': skier[2], 'y2': skier[3]})
    skier = obstacles.ski(screen, y, objects[5], skier_img)
    skiers.append({'x1': skier[0], 'x2': skier[1], 'y1': skier[2], 'y2': skier[3]})

    death = obstacles.forest(screen, y, objects[0], grove)
    death_objects.append({'x1': death[0], 'x2': death[1], 'y1': death[2], 'y2': death[3]})
    death = obstacles.forest(screen, y, objects[1], grove)
    death_objects.append({'x1': death[0], 'x2': death[1], 'y1': death[2], 'y2': death[3]})
    forest(screen, y)
    death = obstacles.death_border_function(x, y, death_zone)

    for i in range(len(death_objects)):
        if death == 1:
            break
        if objects[i]['type'] != 4:
            death = obstacles.death_function(x, y, death_objects[i])
        else:
            death = obstacles.death_border_function(x, y, death_objects[i])

    for i in range(len(skiers)):
        if death == 1:
            break
        death = obstacles.conflict(x, y, skiers[i])

    for i in range(len(ice_objects)):
        if ice == 1:
            break
        ice = obstacles.ice_function(x, y, ice_objects[i])

    if ice != 1:
        ice = 0

    if death == 1:
        n = 0

    if y + n >= 1800:
        return [x, 0, n, score + 1, objects, ice]
    return [x, y + n, n, score + 1, objects, ice]


def death_moment(screen, x, y):
    screen.blit(death_img, (540 + x, 40))
