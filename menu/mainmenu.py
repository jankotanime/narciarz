import pygame

def menu(screen, n):
    menu = [pygame.image.load("../img/other/menu1.png"), pygame.image.load("../img/other/menu2.png"), pygame.image.load("../img/other/menu3.png"), pygame.image.load("../img/other/menu4.png")]
    if n==-1: n=3
    if n==4: n=0
    for i in range(4):
        if i==n:
            screen.blit(menu[i], (0, 0))
    return n

def how(screen):
    info = True
    n=1
    while info:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                info = False
            if key[pygame.K_RIGHT]:
                n+=1
                if n==4:
                    n=1
            if key[pygame.K_LEFT]:
                n-=1
                if n==0:
                    n=3
        instr = pygame.image.load("../img/other/instructions.png")
        contr = pygame.image.load("../img/other/controllers.png")
        obj = pygame.image.load("../img/other/objects.png")
        if n==1:
            screen.blit(instr, (0, 0))
        elif n==2:
            screen.blit(contr, (0, 0))
        elif n==3:
            screen.blit(obj, (0, 0))
        pygame.display.update()




