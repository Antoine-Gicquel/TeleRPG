import pygame
import random
from pygame.locals import *
import os
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

exec(open('lib/pygame_functions.py').read())
exec(open('lib/Dialogue.py').read())
exec(open('lib/Menu.py').read())

tilesNames = [x.split('.')[0] for x in os.listdir('res/tiles') if '.jpg' in x]

## The Map class
class Map(object):
    def __init__(self):
        self.tilesDict = dict()
        for tileName in tilesNames:
            self.addTile(tileName)

        self.tiles = []
        self.tilesEvents = []
        self.entities = []

    def addTile(self, tileName):
        self.tilesDict[tileName] = pygame.image.load("./res/tiles/"+tileName+".jpg").convert()

    def initFromFile(self, filename):
        f = open(filename, "r")
        self.tiles = [] # tiles[y][x]
        self.tilesEvents = []
        self.entities = []
        lines = f.readlines()
        for l in lines:
            if len(l)>2:
                self.tiles.append([])
                self.tilesEvents.append([])
                self.entities.append([])
                l = l.split(" ")
                for c in l:
                    if '\n' in c:
                        c = c.split('\n')[0]
                    if '+' in c: # tile+entity
                        ent = c.split('+')[1]
                        # on stocke l'entité
                        self.entities[-1].append(ent)
                        c = c.split('+')[0]
                    else:
                        self.entities[-1].append(None)
                    c = c.split(",")
                    self.tiles[-1].append(c[0])
                    if len(c) == 1:
                        self.tilesEvents[-1].append(None)
                    elif len(c) > 1:
                        self.tilesEvents[-1].append(",".join(c[1:]))


    def refresh(self, posPerso, windowDim):
        global fenetre
        surf = pygame.display.get_surface()
        nbTilesX = math.floor(windowDim[0]/40)+2
        nbTilesY = math.floor(windowDim[1]/40)+2

        xDebut = posPerso[0] - nbTilesX // 2 + 1
        xFin = xDebut + nbTilesX
        yDebut = posPerso[1] - nbTilesY // 2 + 1
        yFin = yDebut + nbTilesY

        for j in range(xDebut, xFin):
            for i in range(yDebut, yFin):
                if (i>=0 and j>=0 and i<len(self.tiles) and j<len(self.tiles[0])):
                    fenetre.blit(self.tilesDict[self.tiles[i][j]], ((j-xDebut)*40, (i-yDebut)*40))
                else:
                    fenetre.blit(self.tilesDict["void"], ((j-xDebut)*40, (i-yDebut)*40))
    
    def canWalk(self, x, y):
        return not (x < 0 or y < 0 or x>= len(self.tiles[0]) or y >= len(self.tiles))
    
    def paintTile(self, pos, tileNb):
        x, y = pos
        self.tiles[y][x] = tilesNames[tileNb]
    
    def saveToFile(self, filename):
        f = open(filename, "w")
        for i in range(len(self.tiles)):
            l = self.tiles[i][:]
            for j in range(len(l)):
                if self.tilesEvents[i][j] != None:
                    l[j] = l[j] + "," + self.tilesEvents[i][j]
                if self.entities[i][j] != None:
                    l[j] = l[j] + "+" + self.entities[i][j]
            f.write(" ".join(l) + "\n")
        f.close()
        pass


## The Cursor class

class Cursor(object):
    def __init__(self):
        surf = pygame.display.get_surface()
        self.position = [0, 0] # en tiles
        self.tile = pygame.image.load('./res/skin/map_editor.png').convert_alpha()
        xPerso = math.floor((surf.get_width()/2 - self.tile.get_rect()[0]/2)/40)*40
        yPerso = math.floor((surf.get_height()/2 - self.tile.get_rect()[1]/2)/40)*40
        self.hitbox = pygame.Rect((xPerso + 1, yPerso + 1), (38, 38))
                
    def afficher(self, windowDim):
        xPerso = math.floor((windowDim[0]/2 - self.tile.get_rect()[0]/2)/40)*40
        yPerso = math.floor((windowDim[1]/2 - self.tile.get_rect()[1]/2)/40)*40
        self.hitbox = pygame.Rect((xPerso + 1, yPerso + 1), (38, 38))
        fenetre.blit(self.tile, (xPerso, yPerso))
    
    def move(self, dx, dy):
        self.position[0] += dx
        self.position[1] += dy
    
    def getPosition(self):
        return self.position

## The main part


creation = input("Creer une map (c) ou reprendre une map existante (r) ? ")
map_name = input("Nom de la map ? ")

# on charge la map
if creation == 'c':
    width = int(input("Largeur ? "))
    height = int(input("Hauteur ? "))
    ligne = ["void" for j in range(width)]
    f = open('res/maps/'+map_name, 'w+')
    for i in range(height):
        f.write(" ".join(ligne) + "\n")
    f.close()


window_dimensions = [800, 600]
pygame.init()
fenetre = pygame.display.set_mode((window_dimensions[0], window_dimensions[1]), pygame.RESIZABLE)
pygame.display.set_caption("Telegame Editor")
map = Map()
map.initFromFile("res/maps/"+map_name)
cursor = Cursor()
map.refresh(cursor.getPosition(), window_dimensions)
cursor.afficher(window_dimensions)
Dialogue("Echap : menu des tiles  -  CTRL + arrow : ne peint pas  -  S : save", pygame.image.load("./res/entities/yves_poilane.png").convert_alpha()).show()
pygame.display.flip()
pygame.key.set_repeat(400, 60)


continuer = 1
current_tile = 0
while continuer == 1:
    needRefresh = False
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
        mods = pygame.key.get_mods()
        if event.key == K_RIGHT:
            if map.canWalk(cursor.getPosition()[0] + 1, cursor.getPosition()[1]):
                cursor.move(1, 0)
                if not (mods & pygame.KMOD_CTRL): map.paintTile(cursor.getPosition(), current_tile)
                needRefresh = True
        if event.key == K_LEFT:
            if map.canWalk(cursor.getPosition()[0] - 1, cursor.getPosition()[1]):
                cursor.move(-1, 0)
                if not (mods & pygame.KMOD_CTRL): map.paintTile(cursor.getPosition(), current_tile)
                needRefresh = True
        if event.key == K_UP:
            if map.canWalk(cursor.getPosition()[0], cursor.getPosition()[1] - 1):
                cursor.move(0, -1)
                if not (mods & pygame.KMOD_CTRL): map.paintTile(cursor.getPosition(), current_tile)
                needRefresh = True
        if event.key == K_DOWN:
            if map.canWalk(cursor.getPosition()[0], cursor.getPosition()[1] + 1):
                cursor.move(0, 1)
                if not (mods & pygame.KMOD_CTRL): map.paintTile(cursor.getPosition(), current_tile)
                needRefresh = True
        if event.key == K_ESCAPE:
            current_tile = Menu("En quoi je peint ?", tilesNames).show(True)
        if event.key == K_s:
            map.saveToFile("res/maps/"+map_name)
            

    if needRefresh:
        map.refresh(cursor.getPosition(), window_dimensions)
        cursor.afficher(window_dimensions)
        pygame.display.flip()

pygame.display.quit()
pygame.quit()