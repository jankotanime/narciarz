import pygame


def name(nick):
    key = pygame.key.get_pressed()
    for i in range(pygame.K_a, pygame.K_z + 1):
        if key[i]:
            nick.append(chr(i))
    for i in range(pygame.K_1, pygame.K_9 + 1):
        if key[i]:
            nick.append(chr(i))
    if key[pygame.K_0]:
        nick.append("0")
    if key[pygame.K_SPACE]:
        nick.append(" ")
    return nick


def rank_check(score):
    with open('../menu/bests', 'r') as file:
        values = [int(line.strip()) for line in file]
    if values:
        new_tab = score_search(values[0], values[len(values)-1], values, score)
    else:
        new_tab = [score]
    if new_tab == values:
        return False
    else:
        x = 0
        with open('../menu/bests', 'w') as file:
            for i in range(len(new_tab)):
                file.write(str(new_tab[i]))
                file.write('\n')
                if new_tab[i] == score:
                    x = i
        return x + 1


def score_search(hight, low, values, score):
    new_tab = []
    if score > hight:
        new_tab.append(score)
        if len(values) != 5:
            for i in range(len(values)):
                new_tab.append(values[i])
        else:
            for i in range(4):
                new_tab.append(values[i])
    elif score < low:
        if len(values) == 5:
            return values
        else:
            for i in range(len(values)):
                new_tab.append(values[i])
            new_tab.append(score)
    else:
        for i in range(len(values) - 1):
            if values[i] > score:
                new_tab.append(values[i])
            else:
                new_tab.append(score)
                break
        if len(values) != 5:
            for i in range(len(new_tab) - 1, len(values)):
                new_tab.append(values[i])
        else:
            for i in range(len(new_tab) - 1, 4):
                new_tab.append(values[i])
    return new_tab


def name_overwrite(x, new_name):
    with open('../menu/players', 'r') as file:
        players = file.readlines()
    with open('../menu/players', 'w') as file:
        for i in range(x):
            file.write(players[i])
        file.write(new_name)
        file.write("\n")
        if len(players) != 5:
            for i in range(x, len(players)):
                file.write(players[i])
        else:
            for i in range(x, 4):
                file.write(players[i])
