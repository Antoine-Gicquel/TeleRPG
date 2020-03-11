class Map(object):
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.tilesDict = dict()
        tilesNames = [x.split('.')[0] for x in os.listdir('res/tiles') if '.jpg' in x]
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
                        self.entities[-1].append(Entity.createEntity(ent))
                        c = c.split('+')[0]
                    else:
                        self.entities[-1].append(None)
                    c = c.split(",")
                    self.tiles[-1].append(c[0])
                    if len(c) == 1:
                        self.tilesEvents[-1].append(None)
                    elif len(c) > 1:
                        if c[1] == 'event_porte':
                            self.tilesEvents[-1].append(DoorConnector(c[2], (int(c[3]), int(c[4])))) # mapToGo, xToGoInMap, yToGoInMap

    def refresh(self, posPerso, windowDim):
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
                    self.fenetre.blit(self.tilesDict[self.tiles[i][j]], ((j-xDebut)*40, (i-yDebut)*40))
                    if self.entities[i][j] != None:
                        self.fenetre.blit(self.entities[i][j].getImage(), ((j-xDebut)*40, (i-yDebut)*40))
                else:
                    self.fenetre.blit(self.tilesDict["void"], ((j-xDebut)*40, (i-yDebut)*40))

    def canWalk(self, x, y):
        global entityToInteract
        if (x < 0 or y < 0 or x>= len(self.tiles[0]) or y >= len(self.tiles)):
            return False
        if self.tiles[y][x] in ["orange", "void"] or self.checkEntity((x,y)):
            return False
        return True

    def checkEvent(self, playerPos):
        return self.tilesEvents[playerPos[1]][playerPos[0]] != None

    def getEvent(self, playerPos):
        c = self.tilesEvents[playerPos[1]][playerPos[0]]
        return c
    
    def checkEntity(self, playerPos):
        return self.entities[playerPos[1]][playerPos[0]] != None

    def getEntity(self, playerPos):
        c = self.entities[playerPos[1]][playerPos[0]]
        return c
