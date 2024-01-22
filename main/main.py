import pygame
import object.functions as play
import menu.mainmenu as menu
import static
import menu.ranking as ranking

NoName = ('N', 'o', 'N', 'a', 'm', 'e')

pygame.init()

game = False
lost = False
control = 0

name = []

lost_change = 0

cords = [0, 0, 3, 0, [{'type': 1, 'start': 900},
                      {'type': 3, 'start': 1800},
                      {'type': 2, 'start': 3000},
                      {'type': 1, 'start': 3000},
                      {'type': [0, 3], 'start': 3000},
                      {'type': [1, 3], 'start': 0}, 0]]

pygame.display.set_caption('Shroom Collector')
screen = pygame.display.set_mode((static.SCR_WITDH, static.SCR_HEIGT))

run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(360)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            run = False
        if game:
            if cords[5] != 1:
                if key[pygame.K_LEFT]:
                    control = 1
                elif key[pygame.K_RIGHT]:
                    control = 2
                elif key[pygame.K_DOWN]:
                    control = 0
        elif lost:
            name = menu.lost(screen, cords[3], name, key)
            ranking.show_nick(screen, name)
            pygame.display.update()
            if key[pygame.K_BACKSPACE] and len(name) > 0:
                del name[len(name) - 1]
            if key[pygame.K_RETURN]:
                change_ranking = ranking.rank_check(cords[3])
                if change_ranking:
                    if not name:
                        name = NoName
                    ranking.name_overwrite(change_ranking - 1, "".join(map(str, name)))
                lost = False
                control = 0
                control = menu.menu(screen, control)
        else:
            if key[pygame.K_DOWN]:
                control += 1
                control = menu.menu(screen, control)
            elif key[pygame.K_UP]:
                control -= 1
                control = menu.menu(screen, control)
            elif key[pygame.K_SPACE]:
                if control == 0:
                    name = []
                    lost_change = 0
                    cords = [0, 0, 3, 0, [{'type': 1, 'start': 900},
                                          {'type': 3, 'start': 1800},
                                          {'type': 2, 'start': 3000},
                                          {'type': 1, 'start': 3000},
                                          {'type': [0, 3], 'start': 3000},
                                          {'type': [1, 3], 'start': 0}, 0]]
                    score = 0
                    game = True
                elif control == 1:
                    menu.how(screen)
                elif control == 2:
                    menu.top(screen)
                else:
                    run = False
            menu.menu(screen, control)
    if game:
        if cords[2] == 0:
            control = 0
            lost = True
            game = False
            menu.lost(screen, cords[3], name, key)
        else:
            cords = play.move(screen, cords[0], cords[1], cords[2], cords[3], cords[4], control)
    pygame.display.update()
pygame.quit()
