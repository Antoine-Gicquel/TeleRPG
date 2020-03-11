import pygame
import random
from pygame.locals import *
import os
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))
exec(open('lib/pygame_functions.py').read())
exec(open('lib/Entity.py').read())
exec(open('lib/Perso.py').read())
exec(open('lib/Event.py').read())
exec(open('lib/Map.py').read())
exec(open('lib/Dialogue.py').read())
exec(open('lib/Menu.py').read())


window_dimensions = [800, 600]
pygame.init()
fenetre = pygame.display.set_mode((window_dimensions[0], window_dimensions[1]), pygame.RESIZABLE)
pygame.display.set_caption("Telegame")
perso = Perso(fenetre)
map = Map(fenetre)
map.initFromFile("./res/maps/map_outside")
perso.position = [80, 46]
entities = []
map.refresh(perso.getPosition(), window_dimensions)
perso.afficher(window_dimensions)
pygame.display.flip()
pygame.key.set_repeat(400, 60)

# son = pygame.mixer.Sound("pomme.wav")
# mort = pygame.mixer.Sound("game-over.wav")
# pygame.time.delay(3720)


continuer = 1
while continuer == 1:
    needRefresh = False
    # pygame.event.wait()
    event = pygame.event.wait()
    if event.type == QUIT:
        continuer = 0
        needRefresh = True
    if event.type == VIDEORESIZE:
        window_dimensions = [event.w, event.h]
        fenetre = pygame.display.set_mode((event.w, event.h),
                                            pygame.RESIZABLE)
        needRefresh = True
        
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            if map.canWalk(perso.getPosition()[0] + 1, perso.getPosition()[1]):
                perso.move(1, 0)
                needRefresh = True
        if event.key == K_LEFT:
            if map.canWalk(perso.getPosition()[0] - 1, perso.getPosition()[1]):
                perso.move(-1, 0)
                needRefresh = True
        if event.key == K_UP:
            if map.canWalk(perso.getPosition()[0], perso.getPosition()[1] - 1):
                perso.move(0, -1)
                needRefresh = True
        if event.key == K_DOWN:
            if map.canWalk(perso.getPosition()[0], perso.getPosition()[1] + 1):
                perso.move(0, 1)
                needRefresh = True
        if event.key == K_e:
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if map.checkEntity((perso.getPosition()[0] + dx, perso.getPosition()[1] + dy)):
                    map.getEntity((perso.getPosition()[0] + dx, perso.getPosition()[1] + dy)).runScenario()
                    break


    # Gestion des evenements de map
    if map.checkEvent(perso.getPosition()):
        ev = map.getEvent(perso.getPosition())
        ev.act()
        needRefresh = True


    
    if needRefresh:
        visual_refresh()

pygame.display.quit()
pygame.quit()