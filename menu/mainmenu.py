import pygame
import menu.ranking as ranking

best_players = pygame.image.load("../img/other/top_players.png")


def menu(screen, n):
    menu_img = [pygame.image.load("../img/other/menu1.png"), pygame.image.load("../img/other/menu2.png"),
                pygame.image.load("../img/other/menu3.png"), pygame.image.load("../img/other/menu4.png")]
    if n == -1:
        n = 3
    if n == 4:
        n = 0
    for i in range(4):
        if i == n:
            screen.blit(menu_img[i], (0, 0))
    return n


def how(screen):
    info = True
    n = 1
    while info:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                info = False
            if key[pygame.K_RIGHT]:
                n += 1
                if n == 4:
                    n = 1
            if key[pygame.K_LEFT]:
                n -= 1
                if n == 0:
                    n = 3
        instr = pygame.image.load("../img/other/instructions.png")
        contr = pygame.image.load("../img/other/controllers.png")
        obj = pygame.image.load("../img/other/objects.png")
        if n == 1:
            screen.blit(instr, (0, 0))
        elif n == 2:
            screen.blit(contr, (0, 0))
        elif n == 3:
            screen.blit(obj, (0, 0))
        pygame.display.update()


def lost(screen, score, name):
    lost_img = pygame.image.load("../img/other/lost.png")
    screen.blit(lost_img, (0, 0))
    font = pygame.font.Font('../img/other/Lato-Black.ttf', 64)
    score = str(score)
    text = font.render(score, True, (0, 0, 0), (100, 100, 100))
    screen.blit(text, (500, 250))
    font = pygame.font.Font('../img/other/Lato-Black.ttf', 64)
    nickname = "".join(map(str, name))
    text = font.render(nickname, True, (0, 0, 0), (100, 100, 100))
    screen.blit(text, (500, 500))
    return ranking.name(name)


def top(screen):
    screen.blit(best_players, (0, 0))
    font = pygame.font.Font('../img/other/Lato-Black.ttf', 64)
    with open('../menu/players', 'r') as file:
        players = file.readlines()
        text = font.render(str(players), True, (0, 0, 0), (100, 100, 100))
        screen.blit(text, (500, 500))


