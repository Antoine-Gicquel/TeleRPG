import pygame
import random
from pygame.locals import *
import os
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))
exec(open('lib/Perso.py').read())
exec(open('lib/DoorConnector.py').read())
exec(open('lib/Map.py').read())
exec(open('lib/Dialogue.py').read())

window_dimensions = [800, 600]
pygame.init()
fenetre = pygame.display.set_mode((window_dimensions[0], window_dimensions[1]), pygame.RESIZABLE)
pygame.display.set_caption("Telegame")
perso = Perso(fenetre)
map = Map(fenetre)
map.initFromFile("./res/maps/map_o")
entities = []
map.refresh(perso.getPosition(), window_dimensions)
perso.afficher(window_dimensions)
pygame.display.flip()
pygame.key.set_repeat(400, 60)

# son = pygame.mixer.Sound("pomme.wav")
# mort = pygame.mixer.Sound("game-over.wav")
# font = pygame.font.Font("verdana.ttf", 30)
# a_score = font.render(str(score), 1, (255, 255, 255))
# fenetre.blit(a_score, (6,32))
# pygame.time.delay(3720)
# BOUCLE INFINIE


continuer = 1
while continuer == 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == VIDEORESIZE:
            window_dimensions = [event.w, event.h]
            fenetre = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if map.canWalk(perso.getPosition()[0] + 1, perso.getPosition()[1]):
                    perso.move(1, 0)
            if event.key == K_LEFT:
                if map.canWalk(perso.getPosition()[0] - 1, perso.getPosition()[1]):
                    perso.move(-1, 0)
            if event.key == K_UP:
                if map.canWalk(perso.getPosition()[0], perso.getPosition()[1] - 1):
                    perso.move(0, -1)
            if event.key == K_DOWN:
                if map.canWalk(perso.getPosition()[0], perso.getPosition()[1] + 1):
                    perso.move(0, 1)

    # Gestion des collisions
    for ent in entities:
        if perso.getHitbox().colliderect(ent.getHitbox()):
            # on gère la collision
            pass

    # Gestion des evenements de map
    if map.checkAction(perso.getPosition()):
        action, param = map.getAction(perso.getPosition())
        action(param)

    # On recommence
    if continuer == 2:
        continue
    else :
        map.refresh(perso.getPosition(), window_dimensions)
        perso.afficher(window_dimensions)
        pygame.display.flip()
