import pygame
import object.player as player
import menu.mainmenu as menu

pygame.init()

SCR_WITDH=800
SCR_HEIGT=400
game = False
control=0

pygame.display.set_caption('Shroom Collector')
screen = pygame.display.set_mode((SCR_WITDH, SCR_HEIGT))

run = True
while run:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            run = False
        if game==True:
            if key[pygame.K_SPACE]:
                player.move(screen,120, 120)
        else:
            if key[pygame.K_DOWN]:
                control+=1
                control=menu.indicator(screen, control)
            elif key[pygame.K_UP]:
                control-=1
                control=menu.indicator(screen, control)
            elif key[pygame.K_SPACE]:
                if control==0: game=True
                elif control==1: menu.how(screen)

            menu.menu(screen)
            menu.indicator(screen, control)
        pygame.display.update()
pygame.quit()