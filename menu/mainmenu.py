import pygame

def menu(screen):
    menuimg = pygame.image.load("../img/other/menu.png")
    screen.blit(menuimg, (0, 0))

def indicator(screen, n):
    cords=[176, 273, 487, 217, 243, 517, 258, 283, 478, 299, 301, 457]
    left = pygame.image.load("../img/other/left-arrow.png")
    right = pygame.image.load("../img/other/right-arrow.png")
    if n==-1: n=3
    if n==4: n=0
    for i in range(4):
        if i==n:
            screen.blit(left, (cords[n*3+1], cords[n*3]))
            screen.blit(right, (cords[n*3+2], cords[n*3]))
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




