import pygame
import object.player as player
import menu.mainmenu as menu

pygame.init()

SCR_WITDH=800
SCR_HEIGT=400
game = False
control=0

pygame.display.set_caption('Shroom Collecting')
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
            menu.menu(screen)
            if key[pygame.K_DOWN]:
                control+=1
                control=menu.indicator(screen, control)
            if key[pygame.K_UP]:
                control-=1
                control=menu.indicator(screen, control)
            menu.indicator(screen, control)
        pygame.display.update()
pygame.quit()